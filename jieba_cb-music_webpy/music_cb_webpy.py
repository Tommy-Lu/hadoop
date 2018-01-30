#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : .py

import web
import jieba
import jieba.analyse


words_dict = {}
cur_word = 'NULL'

with open('inverted_data.data', 'r') as fd:
	for lines in fd:
		ss = lines.strip().split('\t')
		if len(ss) != 2:
			continue
		key_word = ss[0].strip()
		infor = ss[1].strip()
		
		words_dict[key_word] = infor


def word_in_dict(mywords_dict, words):
	infor_list = []
	for word in words:
		if  word in mywords_dict.keys():
			infor_list.append(mywords_dict[word])
	
	return infor_list


def get_top3_infor(mylist):
	tmp_list = []
	for lt in mylist:
		ss = lt.strip().split('')
		ss = ss[:3]
		for ww in ss:
			w,s = ww.strip().split('')

			tmp_list.append(('\t'.join([w, str(s)])))
	
	return tmp_list


urls = (
	'/' , 'index',
	'/content', 'content',
)

useage ='''
Useage:										
	ip:port/content?content=string.....
exaple:										
	http://127.0.0.1:8888/content?content=百度音乐是中国第一音乐门户
'''

class index:
	def GET(self):
		return useage

class content:
	def GET(self):
		my_list = []
		tmp_lsit = []
		par = web.input()
		content = par.get('content', '')
		words = jieba.analyse.extract_tags(content)
		my_list = word_in_dict(words_dict,words)
		tmp_list = get_top3_infor(my_list)

		#print (tmp_list)
		return "\n".join(tmp_list)

		"""
		for word in words:
			print(word)
			my_word.append(word)
		
		print (my_word)
		return my_word
		"""
	
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()



