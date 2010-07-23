#!/usr/bin/env python
import sys
import csv
from itertools import izip, chain

out = open(sys.argv[1],'w')
inputs = [open(arg,'r') for arg in sys.argv[2:]]
readers = [csv.reader(input) for input in inputs]

for tup in izip(*readers):
	out.write(','.join(list(chain(*tup))))
	out.write('\n')
