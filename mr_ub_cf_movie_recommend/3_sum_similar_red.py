#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : 3_sum_similar_map.py

import sys

uu_cur =None
sum_similar = 0


for lines in sys.stdin:
	ss =lines.strip().split('\t')
	if len(ss) != 2:
		continue
	
	u_u = ss[0].strip()
	si = float(ss[1].strip())

	if not uu_cur:
		uu_cur = u_u
	
	if uu_cur != u_u:
		u1, u2  = uu_cur.strip().split('_')
		print "%s\t%s\t%s" % (u1, u2, sum_similar)
		sum_similar = 0
		uu_cur = u_u

	sum_similar += si

u1, u2  = uu_cur.strip().split('_')
print "%s\t%s\t%s" % (u1, u2, sum_similar)


