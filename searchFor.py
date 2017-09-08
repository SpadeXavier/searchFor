#!/usr/bin/python

# CONSIDER MAKING found_files INTO A DICTIONARY WHICH STORES LINE NUMBERS FOR EACH FILE ALSO ALLOWING THIS SCRIPT TO PRINT OUT EACH LINE NUMBER 

from sys import argv 
import glob 
import os 

os.system('clear') 


try:
	word_to_find = argv[1] 
except IndexError:
	raise IndexError("Please specify a word to search for")

try: 
	# have to use this to get the path of where the script is actually being run from
	directory_path = argv[2]  
except IndexError:
	raise IndexError("Please specify a directory name")

print('------------- SEARCH RESULTS FOR \'' + word_to_find + '\'----------------')
print()


current_path = os.path.dirname(os.path.realpath(argv[1]))
file_paths = glob.glob(current_path + "/" + directory_path + "*") 
found_files = [] 
found_dict = {}

for f in file_paths:
	try:
		with open(f, mode='r') as file:
			try: 
				lines = file.readlines()
				for line in lines:
					if word_to_find in line:
						# appending the file name 
						if f not in found_files: 
							found_files.append(f) 
							found_dict[f] = [] 
						found_dict[f] += [line]
			except:
				pass 
	# Not recursive, have to explicitely search using that directory as argument 
	except IsADirectoryError:
		pass 

from termcolor import colored

file_num = 1
for f in found_files: 
	print(colored('File {}:'.format(file_num), 'red')) 
	start_index = f.find(directory_path)
	print(colored(f[start_index:], 'yellow')) 
	for line in found_dict[f]: 
		print(colored('--> ','blue'), end='')
		print(line, end = '') 
	print() 
	file_num += 1
