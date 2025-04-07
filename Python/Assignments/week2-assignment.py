# Initialize an empty list
my_list = [] 

# Append numbers to the list
for number in [10, 20, 30, 40]:
    my_list.append(number)

#Insert a number at the second position in the list
my_list.insert(1, 15)

#Extend my_list with another list
my_list.extend([50, 60, 70])

#Remove the last element from my_list.
my_list.pop()

#Sort my_list in ascending order.
my_list.sort()

#Find and print the index of the value 30 in my_list.
print(my_list)
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")