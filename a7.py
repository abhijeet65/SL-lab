 
# Write a python program to define a student class that includes
# name, usn and marks of 3 subjects.
# Write functions calculate() - to calculate the sum of the marks
# print() to print the student details. 
class student: 
	usn = " "
	name = " " 
	marks1 = 0
	marks2 = 0
	marks3 = 0
	
	def __init__(self,usn,name,marks1,marks2,marks3): #Constructor 
		self.usn = usn
		self.name = name
		self.marks1 = marks1
		self.marks2 = marks2
		self.marks3 = marks3
			
	def calculate(self): 
	    print ("Total is ", (self.marks1 + self.marks2 + self.marks3))

	def printstudent(self):
		print ("Name is", self.name)
		print ("USN is", self.usn)

print ("Result of Un-named object of student calling calculate ")	    
s1 = student("1MSIS16007", "XYZ", 52,64,88)   
s1.calculate();
s1.printstudent();
