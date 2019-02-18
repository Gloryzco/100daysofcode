from os import system
from time import sleep

class User():	
	def __init__(self, first_name, last_name, sex, email, password):
		"""initialize the properties of a user"""
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.email = email
		self.password = password
		
	def fullname(self):
		"""concatinating firstname and lastname to give the fullname"""
		return '{} {}'.format(self.first_name, self.last_name) 
		
	def describe_user(self):
		"""briefly describing the user"""
		print("FULLNAME: " + self.fullname())
		print("AGE: " + str(self.age))
		
		
		
	def login_user(self):		
		print("\nSUPPLY YOUR CREDENTIALS")
		em = input("\nEnter your email: ")
		pin = input("Enter your password: ")
		print("\nverifying...")
		sleep(1.5)
		if self.email == em and self.password == pin:				
			user.greeting_user()
		else:
			print("\nYour details are not found in out database")
	
	def greeting_user(self):
		"""a statement to welcome the user"""
		system('cls')
		print("\n" + self.fullname().title() + ", You are welcome")
		
		
class Admin(User):
	"""the admin user"""
	
	def __init__(self, first_name, last_name, sex, age, password):
		"""initialize the properties of a admin user"""
		super().__init__(first_name, last_name, sex, age, password)
		self.privileges = ['Add Post', 'Delete Post', 'Add User', 'Delete User',]		
	
	def show_privileges(self):
		"""this aspect shows the privileges of the administrator"""
		print("\nThe  admin's privileges are listed below:")
		for i in range(len(self.privileges)):
			print (str(i+1) + ".  " + self.privileges[i])
	
	
ch =input("\tLOGIN\n 	\n1.  Admin. \t2.  User\n")
if ch == '1':
	admin1 = Admin("Andrew", "Glory", "Male", "andrewglory32@gmail.com", "gloryzco")
	system('cls')
	pw = input("enter your password: ")
	print("\nverifying...")
	sleep(1.5)
	system('cls')
	if pw == "gloryzco":
		print("Glory, welcome to the admin dashboard\n")
		admin1.show_privileges()
	else:
		print("\n\nPassword incorrect!")
		
elif ch == '2':
	system('cls')
	txt = ("Before you can have access to our platform, kindly register yourself")
	print(txt.upper())
	print("-----------------------------------------------------------------------\n")
	fname = input("FIRSTNAME: ")
	lname = input("LASTNAME: ")
	sex = input("M/F: ")
	age = input("EMAIL: ")
	password = input("GENERATE A PASSWORD: ")
	c_password = input("CONFIRM YOUR PASSWORD: ")	
	
	if password == c_password:
		user = User(fname, lname, sex, age, password)
		print("...rigistering user...")
		sleep(1)
		print("\nRegistration successful!!!")
		sleep(1.5)
		system('cls')
		
		user.login_user()
	else:
		print("\nPassword do not match!")
	

else:
	print("Invalid input!")
	





		
