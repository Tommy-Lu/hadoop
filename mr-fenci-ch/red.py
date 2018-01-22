
import sys
import os

word_list = {}

for lines in sys.stdin:
	ww = lines.strip().split("\t")
	if len(ww) != 2:
		continue
	word = ww[0]
	if word not in word_list.keys():
		word_list[word] = 1
	else:
		word_list[word] += 1

word_list = sorted(word_list.iteritems(), key=lambda x : x[1], reverse = True)

for word in word_list:
	print "\t".join([word[0], str(word[1])])



