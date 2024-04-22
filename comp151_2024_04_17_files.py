def read_file():
    filename = 'siddhartha'
    with open(filename) as f_obj:
        contents = f_obj.read()
    print(contents)


def read_lines():
    filename2 = 'student_names'
    with open(filename2) as f_obj:
        # contents = f_obj.read()
        for line in f_obj:
            print(line.rstrip())


# read_file()
# read_lines()
