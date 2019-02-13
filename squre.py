# Write a Python function to create and print a list where 
# the values are square of numbers between any two input integer values.
# both integer inclusive

def squ_num(num1, num2):
	
	if num1 > num2:
		print("\nthe start integer must not be greater than the finishing integer")
	elif num1 < num2:
		for i in range(num1,num2+1):
			squ = i**2
			square_num.append(squ)
			
		print(square_num, end = ", ")
		
square_num = []

num = int(input("enter the start number: "))
num2 = int(input("enter the finish number: "))

squ_num(num, num2)
