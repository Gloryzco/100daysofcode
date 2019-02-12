#A python program that allows user to register theie information based
#on username, password, gender and state using dictionary

num = int(input("how many user would you like to register: "))

users = []
user = {}

for i in range(num):
	print("\n\tUser " + str(i+1))
	username = "username"
	password = "password"
	gender = "gender"
	state = "state"
	
	name = input("\nEnter your username: ")
	pw= input("Enter your password: ")
	sex = input("Enter your gender: ")
	stat = input("Enter your state: ")
	
	user[username] = name
	user[password] = pw
	user[gender] = sex
	user[state] = stat
	
	users.append(user.copy())
	
print("\n")	
for i in range(num):
	print(users[i])
