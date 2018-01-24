#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

for line in sys.stdin:
	ss = line.strip().split("\t")
	if len(ss) != 2:
		continue
	"""
	将输入的中文字符串使用unicode函数来进行utf-8编码，这样为使得单个中文在计数的时候为1，而不是默认的3个字节存储的方式为3.
	这样在后边的访问存储中，一个中文字符都是按照1的单位来读写。
	"""
	str1 = unicode(ss[0].strip(), 'utf-8', errors='ignore' )
	str2 = unicode(ss[1].strip(), 'utf-8', errors='ignore' )
	
	#获取输入字符串的长度，用于计算相似度
	length1 = len(str1)
	length2 = len(str2)

	"""以输入的两个字符串的长度作为2维数组的行和列构建二维数组。
	   注意，构建数组的时候，LCS(Xm, Yn)中，X参数对应数组的行数，Y参数对应数组的列数
	   l = [[0]*3] * 5  ，这里构建5行3列的二维数组
	   为什么要将length1和length2加上1，是因为在从LCS模型构建数组模型的时候，分别多了一行和一列的0.所以要多加上一行和一列。
	"""
	lcs_list = [[0] *  (length2 + 1) ] *  (length1 + 1)
	

	"""以构建的二维来求两个字符串的LCS（最长公共子序列）
	   参看LCS计算的公式
	      LCS(Xm, Yn) = LCS(Xm-1, Yn-1) + xm                //当 xm = yn
	      LCS(Xm, Yn) = max{LCS(Xm-1, Yn), LCS(Xm, Yn-1)}   //当 xm != yn
    """
	for s1 in range(1, length1 + 1):      #这里是因为考虑到使用公式的时候会退1位，以防得到负数，所以取值范围设置为1到length+1
		for s2 in range(1, length2 + 1):
			if str1[s1 - 1] == str2[s2 - 1]:  #从0位置开始判断两个字符串处的字符是否相等，并按照LCS公式进行处理。
				lcs_list[s1][s2] = lcs_list[s1 - 1][s2 - 1] + 1
			else:
				lcs_list[s1][s2] = max(lcs_list[s1 - 1][s2], lcs_list[s1][s2 - 1])

	"""最后一个位置中的值，即为两个字符串最长公共子序列的长度。
	   这里对应为：lcs_list[length1][length2]
	"""
	lcs_value = float(float(lcs_list[length1][length2] * 2 ) / float(length1 + length2) )
	ss = str1+"\t"+str2
	print "\t".join([ss, str(lcs_value) ])   #输出两个字符串和两个字符串的相似度值
	

