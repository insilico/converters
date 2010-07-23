#!/usr/bin/env python
import sys
import csv
import re

def splitrow(row):
	return [row[340 * n : 340 * (n + 1)] for n in range(len(row) / 340 + 1)]

input = open( sys.argv[1], 'r')
output = open( sys.argv[2], 'w')

data = re.compile("^@data$", re.I)

for line in input:
	output.write(line)
	if data.match(line):
		break

tab = csv.reader(input)

for row in tab:
	rows = splitrow(row)
	output.write('\n'.join([','.join(r) for r in rows]) + "\n")
