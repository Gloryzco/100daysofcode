print("HELLO, PLS GIVE US YOUR FEEDBACK ON THIS TUTORIAL\n")
names = []
flag = True
count = 0 
while flag:
	name = input("Enter your name: ")
	feedback = input("your feedback: ")
	count += 1
	names.append(name)

	with open('t_folder\\user_feed.txt', 'a') as fil:
		fil.write("\n\n({})".format(count))
		fil.write("\nNAME: {}".format(name))
		fil.write("\nFEEDBACK: {}".format(feedback))
	
	ch = input("\n\nany other user to give us a feedback? 'y/n': ")
	if ch == 'y':
		flag = True
	elif ch == 'n':
		print('\nThanks, ')
		for i in names:
			print(i, end=', ')
		print('Your feedback helps us to improve and serve you better')
		flag = False
	else:
		print('wrong input')
