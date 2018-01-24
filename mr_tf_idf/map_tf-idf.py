#coding=utf8 

import sys
import math
import os

tf_table = {}
sum_document = 508
word_count = {}

def get_tf_table(tf_tab_file):
	files = open(tf_tab_file,"r")
	for lines in files:
		ss = lines.strip().split('\t')
		if len(ss) != 2:
			continue
		tf_word = ss[0].strip()
		tf_value = ss[1].strip()
		tf_table[tf_word] = float(tf_value)
	
	files.close()
	return tf_table


def map_fun(tf_tab_file):
	tf_table = get_tf_table(tf_tab_file)
	word_set = set()
	for lines in sys.stdin:
		ss = lines.strip().split('\t')
		if len(ss) != 2:
			continue
		file_name = ss[0]
		file_context = ss[1].split(' ')
		for word in file_context:
			word_set.add(word)

		for word in word_set:
			if word not in word_count.keys():
				word_count[word] = 1
			else:
				word_count[word] += 1
		
		word_set = set()
		#for word in word_count.keys():
		#	print word ,word_count[word]
	
	for word in tf_table.keys():
		if word not in word_count.keys():
			#print len(word_count)
			#print len(tf_table)
			#print"Hello"+word
			continue
		else:
			print "\t".join([word, str(math.log(float(sum_document) / float(word_count[word] + 1)))])


if __name__ == "__main__":
	module = sys.modules[__name__]
	func = getattr(module, sys.argv[1])
	args = None
	if len(sys.argv) > 1:
		args = sys.argv[2:]
	func(*args)

	


