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
# It does return a value.
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


