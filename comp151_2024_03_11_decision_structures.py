# Simple conditions, logical connectives, decisions structures
course = 'COMP152'
print(f"course == 'COMP151' is {course == 'COMP151'}.")
print(course == 'COMP152')
# The condition course == 'COMP151' returns a value.
# The returned value has data type known to Python as 'bool'.
print(type(course == 'COMP151'))
# In computer science the true/false data type is called a Boolean.
print(
    f"Check if course is not equal to 'COMP151': course != 'COMP151' is {course != 'COMP151'}.")
print(3 > 4)
classes = ['COMP151', 'COMP152', 'COMP250']
print('COMP152' in classes)
print('MATH095' in classes)
print('au' in 'Laura')

print()

# Explore if statements
print("Exploration of if")
age = 55
if age > 54:
    print("You're older than your professor.")
if age < 54:
    print("You're younger than your professor.")
if age == 54:
    print("You're the same age as your professor.")

print()

print("Here is an if-else")
if age < 54:
    print("You are younger than your professor.")
else:
    print("You are not younger than your professor.")

print()
print("Here is an if-elif-else chain")
if age > 54:
    print("You are older than your professor.")
elif age < 54:
    print("You are younger than your professor.")
else:
    print("You are the same age as your professor.")



