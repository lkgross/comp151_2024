# Discussion about returned values
# Exploration of lists

# The function type returns a value.
type("Hello")
# To see the value, wrap a print around the call to type.
print(type("Hello"))

print()

# The calculation 2 * 3 returns a value.
2  * 3
# To see the value, wrap a print around the calculation.
print(2 * 3)

print()

# Variable assignment does not return a value.
x = 10

# The float function returns a value.
x = 6
float(x)
# To see the value, wrap a print around the call to float.
print(float(x))

# The int function returns a value.
y = 6.8
int(y)
# To see the value, wrap a print around the call to int.
print(int(y))

print()

# The len function returns a value.
countries = ['Brazil', 'US', 'China', 'Haiti']
len(countries)
# To see the value, wrap a print around the call to len.
print(len(countries))

print()

# The sorted function returns a value.
sorted(countries)
# To see the value, wrap a print around the call to sorted.
print(sorted(countries))

print()

countries_sorted = sorted(countries)
print(countries_sorted)
# Calling the sorted method, sorts a list temporarily.
# The countries list is unchanged.
print(f"The countries list looks the same as before we called"
      f" the sorted function: {countries}")
print(f"The sorted version was stored in countries_sorted:"
      f" {countries_sorted}")

print()

# The append method adds an element to the end of a list.
# It does not return a value.
countries.append('Cabo Verde')
print(f"After calling the append method on countries, "
      f"the list is changed: {countries}")

# We can store a sorted version for future use.
countries_sorted = sorted(countries)
print(f"Now the sorted country list is {countries_sorted}")

# Insert method inserts a given element at a given index.
# It does not return a value.
countries_sorted.insert(4, 'Italy')
print(f"After calling the insert method on countries_sorted, "
      f"the list is changed: {countries_sorted}")

print()

num_list = [3, 7, -12, 0, -25, 100, 8]
# The max function returns the maximum number in a list of numbers.
max(num_list)
# To see the returned value, wrap a print around the call to max.
print(max(num_list))

print()

print(f"The sum of the elements is {sum(num_list)}.")

print()

student = "YI yi SUN"
# The title method returns a value.
print("The returned value can be printed or otherwise used:")
print(student.title())

print(f"After calling the title method on student, the value of student remains unchanged: {student}.")
print("Unlike lists, strings are not mutable.")

print()

print("Delete an element by index using the del keyword.")
print(countries_sorted)
del countries_sorted[-1]
print(countries_sorted)

print()

print(countries)
# The remove method does not return a value.
print(countries.remove("US"))
# You can see that no value was returned (except for None).
print()
print(countries)

# None is its own data type.
print(type(None))

countries.append("Ukraine")
countries.append("Brazil")

print()
print(countries)

print()

countries.remove("Brazil")
print(countries)

print()
countries.insert(1, "US")
print(countries)

del countries[1]
print()
print(countries)

print()
countries.insert(1, "US")
print(countries)
# The pop method called with no parameters RETURNS the last element (pops it from the end of the list.
print(countries.pop())
print(countries)
print("Pop from index 1:")
print(f"The returned value is {countries.pop(1)}.")
print(countries)
print("Pop removes an element. It modifies the list.")

print()

print("Slicing is for working with a subset of a list.")
print(countries_sorted)
countries_sorted.append("US")
countries_sorted.insert(0, "US")
print(countries_sorted)
# Slice from index 1 up to and not including 6:
countries_sorted = countries_sorted[1:6]
print(countries_sorted[1:6])

print()
day = ["train", "meeting", "comp151", "comp150", "drop-in hours", "train"]
print(day[2:4])

print()
# Make a copy of the list in memory with this syntax.
print(countries_sorted)
copy_of_countries_sorted = countries_sorted[:]
# Don't omit the [:]. Don't do a reference copy!

