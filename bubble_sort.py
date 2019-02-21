length = int(input("Enter the length of the list: "))
List = []

for i in range(length):
    element = int(input("Enter element: "))
    List.append(element)

# outputing the unsorted list
print("\nthe initial list")
print(List)

# Looping through the list element
print("\nthe sorting iteration")
for j in range(length):

    swapped = False
    i = 0
    while i < length-1:

        # let compare the two close elements and swap where needful
        if List[i] > List[i+1]:
            List[i], List[i+1] = List[i+1], List[i]

            # if swapping occured, the value changes to true
            swapped = True
        i = i+1
        print(List)
    
        # let stop the loop if nothing is swapped i.e list already sorted
        if swapped == False:
            break
