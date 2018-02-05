#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : 1_normalized_red.py



import sys
import math

user_cur = None
movie_rating_list = []

for lines in sys.stdin:
	ss = lines.strip().split('\t')
	if len(ss) != 3:
		continue
	
	userID = ss[0].strip()
	movieID = ss[1].strip()
	Rating = float(ss[2].strip())

	if not user_cur:
		user_cur = userID
	
	if user_cur != userID:
		sum_rating = 0
		for movieid, rating in movie_rating_list:
			sum_rating += rating * rating
		for movieid, rating in movie_rating_list:
			print "%s\t%s\t%s" % (user_cur, movieid, rating / math.sqrt(sum_rating))

		movie_rating_list = []
		user_cur = userID
	
	movie_rating_list.append((movieID, Rating))

sum_rating = 0
for movieid, rating in movie_rating_list:
	sum_rating += rating * rating
for movieid, rating in movie_rating_list:
	print "%s\t%s\t%s" % (user_cur, movieid, rating / math.sqrt(sum_rating))


