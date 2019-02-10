#this program pick up the top two clubs in a 
#group of five to qualify for the round of 16

#points are awarded to each clubs from games played

clubs = {
	'Chelsea': 5,
	'Arsenal': 7,
	'ManCity': 5,
	'Fullham': 3,
	'Burnley': 6,
	}
for c, p in clubs.items():
	print(c + "\t|\t" + str(p))
print("\n=====================\n")

#arranging them in order of decreasing points

winner = (sorted(clubs, key=clubs.__getitem__,reverse=True))
print(winner)


	
	
		
	
		

