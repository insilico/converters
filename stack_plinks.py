#!/usr/bin/env python
import sys
import csv
from itertools import izip, chain

out = sys.argv[1]
ins = sys.argv[2:]

inmaps = [open("%s.map" % i,'r') for i in ins]
outmap = open("%s.map" % out, 'w')
for inmap in inmaps:
	outmap.write(inmap.read())

outmap.close()
map(lambda x: x.close(), inmaps)

outped = open("%s.ped" % out, 'w')
inpeds = [open("%s.ped" % i,'r') for i in ins]
readers = [csv.reader(inped, delimiter="\t") for inped in inpeds]

for tup in izip(*readers):
	head = tup[0]
	tails = [x[2:] for x in tup[1:]]
	outped.write('\t'.join(list(chain(head,*tails))))
	outped.write('\n')

outped.close()
map(lambda x: x.close(), inpeds)
