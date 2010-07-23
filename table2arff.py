#!/usr/bin/env python
import sys
import csv

input = open(sys.argv[1], 'r')
out = sys.argv[2]

attr = open("attr/" + out + ".attr", 'w')

reader = csv.reader(input, delimiter='\t')

columns = []

for row in reader:
	snp,gens = row[0], row[1:]
	#gens = map(lambda x: ''.join(sorted(x)), gens)
	valid = set(gens)
	columns.append(gens)

	attr.write("@ATTRIBUTE %s {%s}\n" % (snp, ','.join(sorted(valid))))

attr.close()

data = open("data/" + out + ".data", 'w')
data.write('\n'.join([','.join(row) for row in zip(*columns)]) + "\n")
data.close()

if __name__ == '__main__':
	sys.exit(main(sys.argv))
