class Nominee():
	def __init__(self, d_fname, d_lname, d_gender, d_phone, d_state):
		self.d_fname = d_fname
		self.d_lname = d_lname
		self.d_gender = d_gender
		self.d_phone = d_phone
		self.d_state = d_state
		
	def fullname(self):
		return '{} {}'.format(self.d_fname, self.d_lname)
		
fname = input("YOUR FIRST NAME: ")
lname = input("YOUR LAST NAME: ")
gender = input("YOUR GENDER 'M/F': ")
phone = input("YOUR PHONE NUMBER: ")
state = input("YOUR STATE: ")

nominee1 = Nominee(fname, lname, gender, phone, state)

print(nominee1.__dict__)

	
