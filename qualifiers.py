# this program pick up the top two clubs in a
# group of five to qualify for the round of 16

group_A = {
    'Team1': {'Name': 'Chelsea', 'point': 2},
    'Team2': {'Name': 'Arsenal', 'point': 6},
    'Team3': {'Name': 'ManCity', 'point': 3},
    'Team4': {'Name': 'Burnley', 'point': 4},
    'Team5': {'Name': 'Everton', 'point': 3},
}

print("\t\tName\t\tPoint")
for team, team_info in group_A.items():
    print(team + "\t->\t" + team_info['Name'] +
          "\t|\t" + str(team_info['point']))
print("\n================================================\n")

# Arranging them in order of decreasing points
print("Arranging them in order of decreasing points\n")
sorted_point = sorted(group_A, reverse=True,
                      key=lambda x: (group_A[x]['point']))
print(sorted_point)
print("\n================================================")

# Outputting the two that qualifies based on points
print("\n\nOutputting the two that qualifies based on points\n")
print(sorted_point[:2])