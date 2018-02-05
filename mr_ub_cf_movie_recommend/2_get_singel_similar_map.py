#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : 2_get_singel_similar_map.py


import sys



for lines in sys.stdin:
	ss = lines.strip().split('\t')
	if len(ss) != 3:
		continue
	
	userID = ss[0].strip()
	movieID = ss[1].strip()
	rating = float(ss[2].strip())

	print "%s\t%s\t%s" % (movieID, userID, rating)
