#!/usr/bin/python
# -*- coding: utf-8 -*-
#file name : .py

import web
import jieba
import jieba.analyse

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
		my_word = []
		par = web.input()
		content = par.get('content', '')
		words = jieba.analyse.extract_tags(content)
		for word in words:
			print(word)
			my_word.append(word)
		
		print (my_word)
		return my_word
	
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()



