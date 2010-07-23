#!/usr/bin/env python
import sys
import getopt
from os import system

def main(argv):
	cmd = argv.pop(0).split('/')[-1]
	help = """Usage: %s OPTIONS INPUT OUTPUT
Converts from Affymetrix format to PLINK MAP/PED file.

Example:
	%s -c 1 -p 0 input output
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

	if argc != 2:
		print help
		return 1

	input,output = args

	return system("./affx2csv.py %s | ./csv2plink.py -c %s -p %s %s" % (input, chrom, phen, output))

if __name__ == '__main__':
	sys.exit(main(sys.argv))
