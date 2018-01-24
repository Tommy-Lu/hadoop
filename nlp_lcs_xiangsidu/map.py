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
	������������ַ���ʹ��unicode����������utf-8���룬����Ϊʹ�õ��������ڼ�����ʱ��Ϊ1��������Ĭ�ϵ�3���ֽڴ洢�ķ�ʽΪ3.
	�����ں�ߵķ��ʴ洢�У�һ�������ַ����ǰ���1�ĵ�λ����д��
	"""
	str1 = unicode(ss[0].strip(), 'utf-8', errors='ignore' )
	str2 = unicode(ss[1].strip(), 'utf-8', errors='ignore' )
	
	#��ȡ�����ַ����ĳ��ȣ����ڼ������ƶ�
	length1 = len(str1)
	length2 = len(str2)

	"""������������ַ����ĳ�����Ϊ2ά������к��й�����ά���顣
	   ע�⣬���������ʱ��LCS(Xm, Yn)�У�X������Ӧ�����������Y������Ӧ���������
	   l = [[0]*3] * 5  �����ﹹ��5��3�еĶ�ά����
	   ΪʲôҪ��length1��length2����1������Ϊ�ڴ�LCSģ�͹�������ģ�͵�ʱ�򣬷ֱ����һ�к�һ�е�0.����Ҫ�����һ�к�һ�С�
	"""
	lcs_list = [[0] *  (length2 + 1) ] *  (length1 + 1)
	

	"""�Թ����Ķ�ά���������ַ�����LCS������������У�
	   �ο�LCS����Ĺ�ʽ
	      LCS(Xm, Yn) = LCS(Xm-1, Yn-1) + xm                //�� xm = yn
	      LCS(Xm, Yn) = max{LCS(Xm-1, Yn), LCS(Xm, Yn-1)}   //�� xm != yn
    """
	for s1 in range(1, length1 + 1):      #��������Ϊ���ǵ�ʹ�ù�ʽ��ʱ�����1λ���Է��õ�����������ȡֵ��Χ����Ϊ1��length+1
		for s2 in range(1, length2 + 1):
			if str1[s1 - 1] == str2[s2 - 1]:  #��0λ�ÿ�ʼ�ж������ַ��������ַ��Ƿ���ȣ�������LCS��ʽ���д���
				lcs_list[s1][s2] = lcs_list[s1 - 1][s2 - 1] + 1
			else:
				lcs_list[s1][s2] = max(lcs_list[s1 - 1][s2], lcs_list[s1][s2 - 1])

	"""���һ��λ���е�ֵ����Ϊ�����ַ�������������еĳ��ȡ�
	   �����ӦΪ��lcs_list[length1][length2]
	"""
	lcs_value = float(float(lcs_list[length1][length2] * 2 ) / float(length1 + length2) )
	ss = str1+"\t"+str2
	print "\t".join([ss, str(lcs_value) ])   #��������ַ����������ַ��������ƶ�ֵ
	

