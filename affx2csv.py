#!/usr/bin/env python
import sys

def convert(infile, outfile):
	row_number = 0
	headers = ['snpid']
	csvrow = []
	last_snp = ''

	for line in infile:
		snp,subj,genotype,_ = line.split()
		# new snp name
		if snp != last_snp:
			row_number += 1
			if row_number == 2:
				outfile.write(','.join(headers))
				outfile.write('\n')
			if row_number > 1:
				outfile.write(','.join(csvrow))
				outfile.write('\n')

			csvrow = [snp]
			last_snp = snp

		if row_number == 1:
			headers.append(subj)
		csvrow.append(genotype)

	outfile.write(','.join(csvrow))
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
