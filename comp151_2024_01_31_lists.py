# A list is a collection of items in a particular order.
list1 = [1,2,3,4,5,6,7,8]
numbers = [1,2,3,4,5,6,7]
friends = ['val', 'bob', 'mia']
roster = ['brandon', 'nick', 'burton', 'josh', 'andrew', 'nathan']
print(list1)

print(type(roster))

# There are 8 elements in list1.
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[7])
print(f"The element at index 2 in roster is {roster[2]}.")
print(friends[-1])
print(f"The element at the end of roster is {roster[-1]}.")

# We can find the length of a list.
print(len(roster))
print(f"The length of list1 is {len(list1)}.")
print(type(list1))
print(type((list1[0])))

# Call the sorted function to return the (temporarily) sorted list.
print(sorted(friends))
# The original list is unchanged.
print(friends)

print(sorted(friends, reverse=True))
print(roster)
# We index into the list with square brackets [] to access
# an element in the list.
print(f"The element at index 4 in roster is {roster[4]}.")
# We can index into a string to access a character in the
# string.
print('andrew'[4])
# Use indexing to modify the elements in the list.
roster[3] = 'john'
# Lists are mutable: They can be changed with indexing.
print(roster)

print()

student_name = 'andrew'
# We can't use indexing to modify the elements of a string.
# student_name[4] = 'y'
# Strings are immutablel
print(student_name)

print()

# Overwrite the element second from the end with 'ronald'.
print(roster[-2])
roster[-2] = 'ronald'
print(roster)

print()

# Add or append 'alex' onto the end of the list.
roster.append('alex')
# The original list is changed.
print(roster)

print()

# We can insert an element at a certain index.
roster.insert(1, 'luis')
# The original list is changed.
print(roster)

print(sorted([3, 17, -1, 0, 5, 12, -6]))