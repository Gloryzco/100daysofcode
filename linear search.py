#A python to:
# >> find a particular number in a list of numbers
# >> find the number of times that number appears in the list
# >> find the position or index of that number in the list

length = int(input("Enter the length of the list: "))

number = []

#getting the array element from user
for i in range(length):
	key = int(input("Enter List element " + str(i) + ": "))
	number.append(key)

#outputing the list
print("\n====================================\n")
print("The list contains the following numbers: ")
print(number)
print("\n====================================\n")

#prompt the user on a key to search
search_key = int(input("Enter the number you want to search: "))

#check if the number entered exist in the list
if search_key not in number:
	print("\n" + str(search_key) + " does not exist in the list")
else:
	#count the number of times it occurs/appear
	count = 0
	for i in range(length):
		if search_key == number[i]:
			count = count + 1
	if count == 1:		
		print("\n" + str(search_key) + " appears " + str(count) + " time in the list")
	else:
		print("\n" + str(search_key) + " appears " + str(count) + " times in the list")
	
	#find the position or index of that number in the list
	print("\nThe number is in index: ")
	for i in range(length):
		if search_key == number[i]:
			print(str(i))
