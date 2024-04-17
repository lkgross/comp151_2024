filename = 'siddhartha'

with open(filename) as f_obj:
    contents = f_obj.read()

print(contents)

filename2 = 'student_names'

with open(filename2) as f_obj:
    # contents = f_obj.read()
    for line in f_obj:
        print(line.rstrip())

# print(contents)

