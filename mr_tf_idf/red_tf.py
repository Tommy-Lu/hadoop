import sys

sum_count = 0  # all words count 
words_dict = {}

for lines in sys.stdin:
	ss = lines.strip().split("\t")
	if len(ss) != 2:
		continue
	sum_count += 1
	word , val = ss
	if word not in words_dict.keys():
		words_dict[word] = 1
	else:
		words_dict[word] += 1
	
#words_dict[key=word,value=word count] 
for word in words_dict.keys():
	#words_tf[word] = double(words_dict[word]) / double(sum_count)
	print "\t".join([word, str(float(words_dict[word]) / float(sum_count))])		
