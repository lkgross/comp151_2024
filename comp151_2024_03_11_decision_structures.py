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
print('a' in 'Laura')
