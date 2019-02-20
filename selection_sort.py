length = int(input("Enter the length of the list: "))
List = []

for i in range(length):
    element = int(input("Enter element: "))
    List.append(element)

print("\nTHE UNSORTED LIST: ")
print(List, "\n\n")

i = 0
while i < length:
    smallest = min(List[i:])

    index_of_smallest = List.index(smallest)

    List[i], List[index_of_smallest] = List[index_of_smallest], List[i]
    i = i + 1
    print(List)
