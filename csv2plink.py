#!/usr/bin/env python
import sys
import getopt
import csv

def csv2pedmap(csvin, pedout, mapout, chromosome, phenotype):
	"""Convert a CSV with SNPs as rows and subjects as columns to PLINK
	PED/MAP files.

	Parameters:
		csvin		- Readable filehandle (CSV source)
		pedout		- Writable filehandle (PED target)
		mapout		- Writable filehandle (MAP target)
	"""

	reader = csv.reader(csvin)

	subjects = reader.next()[1:]
	
	columns = [row for row in reader]

	rows = zip(*columns)

	snps = rows.pop(0)
	
	writeMAP(mapout, chromosome, snps)
	writePED(pedout, subjects, phenotype, rows)

def writeMAP(mapout, chromosome, snps):
	try:
		rowformatstring = str(int(chromosome)) + "\t%s\t1\n"
	except:
		rowformatstring = chromosome + "\t%s\t1\n"
	map(lambda x: mapout.write(rowformatstring % x), snps)

def writePED(pedout, subjects, phenotype, rows):
	rowformatstring = "%s\t" + phenotype + "\t%s\n"
	for subj,row in zip(subjects,rows):
		pedout.write(rowformatstring % (subj, '\t'.join([" ".join(g) for g in row])))

def main(argv):
	cmd = argv.pop(0).split('/')[-1]
	help = """Usage: %s OPTIONS [INPUT] OUTPUT
Converts from CSV format (SNP,GENOTYPE1,GENOTYPE2,...) to PLINK MAP/PED file.

Example:
	%s -c 1 -c 0 input.csv output
		produces output.map, output.ped
	""" % (cmd,cmd)

	try:
		opts,args = getopt.getopt(argv, "c:p:h", ["chromosome=","phenotype=","help"])
	except getopt.error,msg:
		print msg
		print help
		return 1

	chrom = ""
	phen = ""

	for opt,arg in opts:
		if opt in ("-h","--help"):
			print help
			return 0
		elif opt in ("-c","--chromosome"):
			chrom = arg
		elif opt in ("-p","--phenotype"):
			phen = arg
		else:
			print "Unrecognized option %s %s" % (opt, arg)
			print help
			return 1

	if chrom == "" or phen == "":
		print "Chromosome and phenotype options are required"
		print help
		return 1
	
	argc = len(args)

	if not argc:
		print help
		return 1

	out = args.pop()
	argc -= 1

	if argc:
		infile = open(args[0], 'r')
	else:
		infile = sys.stdin

	ped = open("%s.ped" % out, 'w')
	map = open("%s.map" % out, 'w')

	csv2pedmap(infile, ped, map, chrom, phen)

	infile.close()
	ped.close()
	map.close()

if __name__ == '__main__':
	sys.exit(main(sys.argv))
