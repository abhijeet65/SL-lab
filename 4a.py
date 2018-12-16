4.  
# Write a python program 
# to read in a list of numbers.
# Use one-line comprehensions to create a new list of even numbers.
# Create another list reversing the elements.

# read elements  to list M = [x for x in S if x % 2 == 0]

# Read a list of numbers
input_list = eval(input("Enter the comma seperated values: \n"))

even_list = [x for x in input_list if x%2 == 0.0]

print ("Even list : ",even_list)
print ("Even reversed list : ",even_list[::-1])
