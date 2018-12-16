import os
import sys
import functools

# Opening
escape = open(sys.argv[1])


# Storing words and occourences in a dictionary
word_dic = {}

for line in escape:
	my_line = line.split()
	for word in my_line:
		w = word_dic.get(word,0)
		word_dic[word] = w+1

print (word_dic)


# Top ten words
# Sorting by values

sorted_list = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
print ("Sorted list by occourences: ")
print (sorted_list)
top_ten_words = sorted_list

top_ten = []
for i in range(10):
	word_tuple = sorted_list[i]
	top_ten.append(len(word_tuple[0]))
	print (word_tuple[0], "Frequency: ", word_tuple[1], "Length: ", len(word_tuple[0]))

print ("10 words with most occourences: \n")
for i in range(10):
	print (top_ten_words[i])


print("Length of top ten words \n")
print (top_ten)

mysum = functools.reduce(lambda x,y: x+y, top_ten)
avg_length = mysum/10

print ("Average Length: ", avg_length)
squares = [x**2 for x in  top_ten if x%2 != 0]
print ("Squares : ", squares)
