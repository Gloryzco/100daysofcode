# A python program to find number of occurrences of a
# given number with out using built-in methods

scores = [2, 5, 3, 1, 2, 3, 8, 8, 9, 0, 5, 1, 6, 4, 5, 2, 6, 7, 2, 8]

num = int(input("enter any number ranging from 1 - 10 \n"))

if num not in scores:
    print("The number you entered is not in the list")
else:
    count = 0
    for i in range(len(scores)):
        if num == scores[i]:
            count = count + 1

    print("The number occured " + str(count) + " times")

# removing repeated elements from the list without using built-in methods
new_scores = []
for i in scores:
    if i not in new_scores:
        new_scores.append(i)
print("Repeated numbers have been removed\n\n")
print(new_scores)


print("Repeated numbers have been removed \n\n")
print(scores)
