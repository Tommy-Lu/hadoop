#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : recommend_movies.py
import sys


#全局变量，获取用户相似度表，并存储在字典中。
uu_similar_dict = {}  

#全局变量，获取movies.dat中电影ID号和电影名字、类型对应表，并存储在字典中。
movie_id_name_dict = {}

#全局变量，从rating-2k.dat中获取用户观看过的所有电影ID列表
watched_movies_dict = {} 

"""
打开movies.dat文件，并获取其中电影ID和电影名字，类型，将其存储在全局变量movie_id_name_dict中。
"""
def get_movie_names_dict():
	movies_file = open("all_datas/movies.dat", "r")
	for lines in movies_file:
		ss = lines.strip().split("::")
		if len(ss) != 3:
			continue

		movieID = ss[0].strip()
		movieName = ss[1].strip()
		movieGenres = ss[2].strip()

		movie_id_name_dict[movieID] = (movieName, movieGenres)

	movies_file.close()

"""
打开rating-2k.dat文件，获取用户观看过的所有电影ID，并存储在watched_movies_dict中
"""
def get_watched_movie_dict():
	rating_file = open("all_datas/rating-2k.dat", "r")
	cur_user = None
	moviesID = []

	for lines in rating_file:
		ss = lines.strip().split("::")
		if len(ss) != 4:
			continue

		userID = ss[0].strip()
		movieID = ss[1].strip()
		movieRating = ss[2].strip()

		if not cur_user:
			cur_user = userID
		if cur_user != userID:
			watched_movies_dict[cur_user] = moviesID

			moviesID = []
			cur_user = userID

		moviesID.append(movieID)
		
		watched_movies_dict[cur_user] = moviesID
	
	rating_file.close()


"""
打开uu-similar.data(mr计算出来的用户相似度表)，获取和输入用户user最相似的top5用户，
返回top5相似用户。
"""
def get_top5_similar_user(user):
	similar_file = open("all_datas/uu-similar.data", "r")
	top5_list = []
	for lines in similar_file:
		ss = lines.strip().split('\t')
		if len(ss) != 3:
			continue
	
		u1 = ss[0].strip()
		u2 = ss[1].strip()
		si = ss[2].strip()

		if u1 == user:
			top5_list.append( (u2, si) )
		
		top5_list.sort(key = lambda x: x[1], reverse = True)

		top5_list = top5_list[:5]

	similar_file.close()
	return top5_list

"""
输入： user  , 需要推荐电影的用户
输入： si_list  ， 和推荐用户最相似的top5 相似用户
输入： watched_dict ，用户和观看过的所有影片的字典
根据输入的用户，和该用户的top5相似用户，将top5用户观看过而user没有观看过的电影(top10)推荐给user
"""
def get_top10_recommend_movies(user, si_list, watched_dict):
	no_rep_movies = set()    # 用于获取user和top5相似用户(6人)所有观看过的电影(去重)
	the_user_watched_movies = set()  # 用户存放被推荐用户自己观看过的电影。

	#获取输入用户观影列表
	user_movies = watched_dict[user]
	for movie in user_movies:
		no_rep_movies.add(movie)
		the_user_watched_movies.add(movie)

	#获取相似用户的观影列表
	for user_sim in si_list:
		si_user = user_sim[0]
		
		si_movies = watched_dict[si_user]
		for movie in si_movies:
			no_rep_movies.add(movie)
	
	#推荐电影top10
	#no_rep_movies - the_user_watched_movies ：得到相似用户观看过而推荐用户没有观看过的电影列表
	re_movies_top10 = []   
	for re_movie in (no_rep_movies - the_user_watched_movies):
		movie_cunt = 0
		for user_sim in si_list:
			si_user = user_sim[0]
			#统计相似用户观看电影的数量
			if re_movie in watched_dict[si_user]:
				movie_cunt += 1
		#将所有电影和观看人数统计添加到列表。	
		re_movies_top10.append((re_movie, movie_cunt))
	
	#将电影观看人数按照观看人数进行降序排序，并取top10
	re_movies_top10.sort(key = lambda x:x[1], reverse = True)
	re_movies_top10 = re_movies_top10[:10]
	
	#输出top10的电影
	for top10_movie, com in re_movies_top10:
		print "Movies ID :%s \t Watched Time in Top5: %s " % (top10_movie, com)
		movie_name, movie_geres = movie_id_name_dict[top10_movie]
		print "%s::%s" % (movie_name, movie_geres)
		print "\n"
#程序入口
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print """
		==========================================================================
		Uage: ID is the user you want to recommend movies to him.
		Command: python recommend_movies.py ID
		Exaple: python recommend_movies.py 9
		==========================================================================
		"""
		exit()
	#从外部传入推荐用户ID
	test_user = sys.argv[1]
	#test_user = "9"
	
	si_top5_list = []

	get_movie_names_dict()
	get_watched_movie_dict()

	si_top5_list = get_top5_similar_user(test_user)

	get_top10_recommend_movies(test_user, si_top5_list, watched_movies_dict)
