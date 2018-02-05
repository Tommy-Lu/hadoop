#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : 3_sum_similar_map.py


import sys

for lines in sys.stdin:
	ss = lines.strip().split('\t')
	if len(ss) != 3:
		continue
	
	u1 = ss[0].strip()
	u2 = ss[1].strip()
	si = float(ss[2].strip())

	print "%s\t%s" % (u1+'_'+u2, si)

