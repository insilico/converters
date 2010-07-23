#!/usr/bin/env python
import sys

def convert(infile, outfile):
	snp_name = ''

	for line in infile:
		row = line.split()
		current_snp_name = row[0]
		# new snp name
		if current_snp_name != snp_name:
			if snp_name != '':  # All but first
				outfile.write('\n')
			outfile.write(current_snp_name)
			snp_name = current_snp_name
		outfile.write(',' + row[2])

	outfile.write('\n')

def main(argv):
	help = """Usage: %s [INPUT [OUTPUT]]
Converts from Affymetrix listing format (SNP SUBJECT GENOTYPE) to tabular.
	""" % argv[0].split('/')[-1]

	length = len(argv)

	if length > 1:
		infile = open(argv[1], 'r')
	else:
		infile = sys.stdin

	if length > 2:
		outfile = open(argv[2], 'w')
	else:
		outfile = sys.stdout

	convert(infile, outfile)

	infile.close()
	outfile.close()

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
