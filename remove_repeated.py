# removing repeated elements from the list without using built-in methods

scores = [2,5,3,1,2,3,8,8,9,0,5,1,6,4,5,2,6,7,2,8]
print("the original list \n")
print(scores)
new_scores = []
for i in scores:
	if i not in new_scores:
		new_scores.append(i);
print("\n\nRepeated numbers have been removed \n");
print(new_scores)
