#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : 2_get_singel_similar_red.py


import sys

movie_cur = None
user_rating_list = []

for lines in sys.stdin:
	ss = lines.strip().split('\t')
	if len(ss) != 3:
		continue

	movieID = ss[0].strip()
	userID = ss[1].strip()
	rating = float(ss[2].strip())
	rating = round(rating, 3)

	if not movie_cur:
		movie_cur = movieID 
	
	if movie_cur != movieID:
		for i in range(0, len(user_rating_list) - 1):
			for j in range(i+1, len(user_rating_list)):
				user_i, rating_i = user_rating_list[i]
				user_j, rating_j = user_rating_list[j]

				print "%s\t%s\t%s" % (user_i, user_j, rating_i * rating_j)
				print "%s\t%s\t%s" % (user_j, user_i, rating_i * rating_j)
		movie_cur = movieID
		user_rating_list = []

	user_rating_list.append((userID, rating))
	

for i in range(0, len(user_rating_list) - 1):
	for j in range(i+1, len(user_rating_list)):
		user_i, rating_i = user_rating_list[i]
		user_j, rating_j = user_rating_list[j]

		print "%s\t%s\t%s" % (user_i, user_j, rating_i * rating_j)
		print "%s\t%s\t%s" % (user_j, user_i, rating_i * rating_j)

