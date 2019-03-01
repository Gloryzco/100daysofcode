from random import randint

# this program help generates a recharge pin

count = 0
for i in range(16):
    print(randint(0,9),end = "")
    count += 1
    if count % 4 == 0:
	    print(" ", end = "")
