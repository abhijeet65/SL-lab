# 2. Write a python program to 
# count the frequency of words in a given file.

# Put your own path here.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
        	return Counter(f.read().split())

print("Number of words in the file : \n",word_count("Faid"), "\n")
