#!/usr/bin/env python
import sys
import getopt
import csv

def zipgen(a,b):
	while True:
		yield (a.next(),b.next())

def stack(in1, in2, out, writeClass=False):
	reader1 = csv.reader(in1, delimiter='\t')
	reader2 = csv.reader(in2, delimiter='\t')

	len1, len2 = 0, 0
	for row1,row2 in zipgen(reader1,reader2):
		if row1[0] != row2[0]:
			out.write("Not the same SNP! %s %s\n" % (row1[0],row2[0]))
			sys.exit(1)
	
		if writeClass and len1 == 0:
			len1, len2 = map(len,(row1,row2))

		out.write('\t'.join(map(str.strip,row1 + row2[1:])) + "\n")

	if writeClass:
		final = ["Class"] + ["1" for i in xrange(1,len1)] + ["0" for i in xrange(1,len2)]
		out.write('\t'.join(final) + "\n")

def main(argv):
	help = """Usage: %s [--class] TABLE1 TABLE2 OUTPUT
Append corresponding rows in two tables.

Add a class row, denoting the first table's columns with 1, and the
second's with 0.

Example:

Table 1:
label1 a b c
label2 g h i

Table 2:
label1 d e f
label2 j k l

Output:
label1 a b c d e f
label2 g h i j k l
Class  1 1 1 0 0 0
	""" % argv[0].split('/')[-1]

	try:
		opts,args = getopt.getopt(argv[1:], "ch", ["class","help"])
	except getopt.error,msg:
		print msg
		return 0

	writeClass = False

	for opt, arg in opts:
		if opt in ('-c', '--class'):
			writeClass = True
		if opt in ('-h', '--help'):
			print help
			return 0

	if len(args) != 3:
		print help
		return 1

	in1 = argv[1]
	in2 = argv[2]
	out = argv[3]
	
	infile1 = open (in1, 'r')
	infile2 = open (in2, 'r')
	outfile = open (out, 'w')

	stack(infile1, infile2, outfile, writeClass)

	infile1.close()
	infile2.close()
	outfile.close()

	return 0

if __name_ '__main__':
	sys.exit(main(sys.argv))
