#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
程序功能：将输入的音乐文件(每行两个部分，每个字符段(str1,str2),中间'\t'分割)，要求将str2进行jieba获取关键词并获取词的权重(tf-idf)值。后按照如下格式输出到hdfs上。
8923169333      擦肩而过 郑源 MV        郑源:3.98492250097 / MV:3.98492250097 / 擦肩而过:3.29177532041
8923192333      Marry Me  翻唱版        翻唱:4.40251015713 / Me:3.98492250097 / Marry:3.98492250097
"""
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

os.system('tar xvzf jieba.tar.gz > /dev/null')
sys.path.append("./")

import jieba
import jieba.analyse

for lines in sys.stdin:
	ss = lines.strip().split('\t')
	if len(ss) != 2: #判断输入字符是否符合规格
		continue
	
	#获取到两个部分的内容
	music_number = ss[0].strip()
	music_name = ss[1].strip()

	"""
	将第二部分内容进行结巴分词并获取关键词及权重。
	注：tm_list用于存放jieba分词后的关键词和权重，格式为[(word, weight), (..), (..)],即数组中元素为元组
	注：extract_tags函数输出为list类型，包含了关键词和权重值。
	"""
	tm_list = []
	#word_list = jieba.analyse.extract_tags(music_name, withWeight=True)
	for word, weight in jieba.analyse.extract_tags(music_name, withWeight=True):
		#print word, weight
		tm_list.append((word, weight))   #将关键词和权重以元组的形式添加到数组中。
	
	#输出要求的格式。 注意.join的用法
	#注意.join([tm[0], str(tm[1])]) for tm in tm_list)的使用
	print "\t".join([music_number, music_name, ' / '.join(':'.join([tm[0], str(tm[1])]) for tm in tm_list) ])
