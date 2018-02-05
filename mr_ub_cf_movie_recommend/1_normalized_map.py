#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : 1_normalized_map.py


import sys

for lines in sys.stdin:
	ss = lines.strip().split("::")
	if len(ss) != 4:
		continue
	
	userID = ss[0].strip()
	movieID = ss[1].strip()
	rating = ss[2].strip()
	timeStamp = ss[3].strip()

	print "%s\t%s\t%s" % (userID, movieID, rating)

