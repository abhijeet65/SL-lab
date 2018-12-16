# 3.
# Write a python program 
# to find the longest words in a file.

filename = '/Users/apple/Desktop/Fin_aid'

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print (longest_word(filename))