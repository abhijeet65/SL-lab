# 1. 
# Write a python program to read in a list of elements.
# Create a new list that holds all 
# the elements minus the duplicates (Use functions).

# NOTE: Use raw_input for python 2.7 and input for python 3.

n = int(input("How many numbers do you want to enter?"))

def read_numbers(n):
	number_list = []
	for i in range(n):
		number = input("Enter the number: ")
		number_list.append(number)
	return number_list

def remove_duplicates(number_list):
	new_list = []
	for number in number_list:
		if number not in new_list:
			new_list.append(number)
	return new_list

def main():
	original_list = read_numbers(n)
	new_list = remove_duplicates(original_list)
	print ("Original list: ", original_list)
	print ("New list: ", new_list)

main()

