"""
Name: merge_files.py
Function: Meger many files into a sigle file,
Input: txt files 
Output: a sigle txt file
UseAge: python merge_files.py input_files_folder

"""
import sys
import os

input_files = sys.argv[1]        #get the input files folder path
merge_file = open("merge_file.txt" , "w")  #Set the generator file 

#get the files name in the input files path and get the new file path ,then open it 
for file_name in os.listdir(input_files):
	file_path = input_files + file_name
	file_open = open(file_path, 'r')
	
	#get the context in input file and save to a list
	tmp_list = []
	for line in file_open:
		tmp_list.append(line.strip())

	#Write the new list file to the merge_file
	#Use this format: file_name "\t" tmp_list
	#print "\t".join([file_name, " ".join(tmp_list)])
	merge_file.write(file_name)
	merge_file.write("\t")
	for context in tmp_list:
		merge_file.write(context)
		merge_file.write(' ')
	merge_file.write("\n")

#close the opened files
merge_file.close()
file_open.close()

