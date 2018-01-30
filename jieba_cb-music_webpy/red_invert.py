#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : red_invert.py



import sys

cur_tag = 'NULL'
tmp_list = []
tmp_sort_list = []

for lines in sys.stdin:
	ss = lines.strip().split('\t')
	if len(ss) != 3:
		continue
	
	music_tag = ss[0].strip()
	music_name = ss[1].strip()
	music_score = ss[2].strip()

	if cur_tag == 'NULL':
		cur_tag = music_tag
	if cur_tag != music_tag:
		tmp_sort_list = sorted(tmp_list, key=lambda x:x[1], reverse=True)
		print '\t'.join([cur_tag, ''.join(''.join([w[0], str(w[1]) ]) for w in tmp_sort_list ) ])
		cur_tag = music_tag
		tmp_list = []
		tmp_sort_list = []

	tmp_list.append( (music_name,music_score) )

tmp_sort_list = sorted(tmp_list, key=lambda x:x[1], reverse=True)
print '\t'.join([cur_tag, '^A'.join('^B'.join([w[0], str(w[1]) ]) for w in tmp_sort_list ) ])

