#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : map_invert.py


import sys

for lines in sys.stdin:
	ss = lines.strip().split('\t')
	if len(ss) != 3:
		continue
	
	music_id = ss[0].strip()
	music_name = ss[1].strip()
	music_token = ss[2].strip().split('')

	for tag_list in music_token:
		tag , score = tag_list.strip().split('')
		print "\t".join([tag, music_name, score])


