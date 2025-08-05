# creating an empty list
my_list = []

# appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting element at index
my_list.insert(1, 15)

# extending a list
other_list = [50, 60, 70]
my_list.extend(other_list)

# removing the last element
my_list.pop()

# sorting the list in ascending order
my_list.sort()

# printing element at index
element_index = my_list.index(30)
print(element_index)