from random import randint

# This is a game of dice played by four.
# each player throw two dice for each round 3x

player1 = []
player2 = []
player3 = []
player4 = []

players = {}

for i in range(1,4):
	print("\tROUND {}\n".format(i))
	for j in range(1,5):
		input("PLAYER {}, press 'enter' to throw: ".format(j))
		die1 = randint(1,6)
		die2 = randint(1,6)
		print("die1: {}".format(die1))
		print("die2: {}\n".format(die2))
		sumDie = die1 + die2
		if j == 1:
			player1.append(sumDie)
		if j == 2:
			player2.append(sumDie)
		if j == 3:
			player3.append(sumDie)
		if j == 4:
			player4.append(sumDie)

players['player1'] = sum(player1)
players['player2'] = sum(player2)
players['player3'] = sum(player3)
players['player4'] = sum(player4)

print(players)

print("")
for elem in sorted(players.items(), key = lambda x: x[1], reverse = True):
	print(elem[0], " : ", elem[1])

print("\nThe winner is Player", max(players.items(), key = lambda x: x[1]))




