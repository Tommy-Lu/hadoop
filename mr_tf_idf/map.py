import sys

for lines in sys.stdin:
	ss = lines.strip().split("\t")
	files_name = ss[0]
	for word in ss[1].strip().split(" "):
		print "\t".join([word, "1"])

	


