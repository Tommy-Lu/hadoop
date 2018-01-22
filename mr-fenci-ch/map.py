import os
import sys

os.system('tar xvzf jieba.tar.gz > /dev/null')
sys.path.append("./")
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba

#get input file from hdfs
for lines in sys.stdin:
	words = jieba.cut(lines, cut_all=False)
	for word in words:
		print "\t".join([word, "1"])


