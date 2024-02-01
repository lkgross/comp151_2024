# Exploration of Week 2 ideas Remember the lines that start with a hashtag
# are comments (for the human reader), rather than code to be executed.

# Store a piece of data like the text "Hello World" in a variable.
# Use the equals sign (=) to assign a value to a variable.
# Use a descriptive name for a variable. Here we use greeting as the name.
greeting = "Hello world"
# The equals sign (=) lets us store the value "Hello world" in the variable.
# (Variable assignment does not produce any output.)

# When you run this file (script), the first lines of output are from:

print("Let's print the value of greeting:")
print(greeting)

# Note the above line of code prints the VALUE of the variable greeting.

print()  # Print a blank line.

# Let's experiment with calculation in Python.
# Try using +, -, *, and / .
# Also try:
print("Let's calculate 2 // 3:")
print(2 // 3)
# It produces a 0.
# The // is an "integer divide", which divides and then drops the decimal part.

print()

# Compare and contrast the output given by these two calculations. Explain.
print("Division 7/4 yields:")
print(7 / 4)
print("Integer division 7//4 yields")
print(7 // 4)
print("because the decimal part is dropped.")
# Note we have printed the values of a couple of calculations (when the file
# is run.)

print()

# Assign some values to variables.
# Always use descriptive names, suggestive of the meanings of the variables.
# Always choose names in lower case in Python.
# Use an underscore (_) to separate words in the name.
# The first character in a variable should be a letter.
class_grade = 4.0
class_credits = 3
quality_points = class_grade * class_credits
print("Quality points:")  # prints the text in quotes
print(quality_points)  # prints the value of the quality_points variable.

print()

# An f-string is a formatted string. Note the syntax print(f"...") . The
# curly brackets {} mean to use the value, e.g., 4.0, rather than the text
# "class_grade".
print(
    f"Class grade {class_grade} * class credits {class_credits} is {class_grade * class_credits}.")

print()

# In Python, you can assign values to two variables on the same line.
c1, c2 = 3, 2
# Don't start variable name with a number like in 1c = 3.
print("c1 is:")
print(c1)
print("c2 is:")
print(c2)
print("c1*c2 is:")
print(c1 * c2)

print()

# Here we assign two values to two variables.
# What is each variable? What is its value?
first_name, last_name = "laura", "gross"
print(first_name)
print(last_name)
# Use an f-string. What happens if you remove the braces {}? Why?
print(f"Is your favorite author {first_name} {last_name}?")

print()

# The type function gives the type of data.

# An integer is an 'int' in Python.

# A decimal number is called a floating-point number in computer science
# ('float' in Python).

# The text data type is called a string in computer science ('str') in Python.

# Print out the data type for the variable greeting:
# Is greeting a string (str)? Is it an integer (int)? Is it a float (float)?
print(f"The data type of the variable greeting is {type(greeting)}.")

# Try things like the following *in the (interactive) Python console*.
type(4)
type(3.7)
type("Jesse")

# We can we print the output from the type command from the editor using
print(type(4))
print(type(3.7))
print(type("Jesse"))
# The output from the type function becomes the input to the print function.
# What questions do you have? Ask them!

print()

# Incrementing a value: Increase the value by 1.
counter = 0
print("The value of counter is:")
print(counter)

print()

# We overwrite the value of counter with 1:
counter = counter + 1
print("The value of counter is:")
print(counter)

print()

# A shorthand to increment the counter is this syntax:
counter += 1
print(counter)

# Use all caps for constants that never change value.
KM_IN_MI = 1.69

print()

# You can use either single quotes ' or double quotes " for a string.
print('Hello World')
# Be careful to use double quotes " if there's a single quote within the string.
# \t and \n
# print("\tSomething that's got\nan apostrophe")

print("laura".upper())
