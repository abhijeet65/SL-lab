ip_list = eval(input("Enter the list comma seprated : "))
even_list = [x for x in ip_list if x%2 == 0.0 ]
print ("Even list : ",even_list)
print ("Even reversed list : ",even_list[::-1])
