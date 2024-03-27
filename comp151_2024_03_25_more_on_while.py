def addition_quiz():
    # Initialize the loop variables.
    # This avoids an error when you hit the while-loop condition.
    response = 0
    not_quit = True
    # Loop variables for the while loop
    # are response and not_quit
    while not(response == 7) and not_quit:
        # Ensure a loop variable is updated in the
        # body of the while loop.
        # This avoids an infinite loop.
        response = input("What is 3 + 4? (Enter q to quit.) ")
        if response != 'q':
            response = int(response)
        else:
            not_quit = False
    if response == 7:
        print("Correct!")

# print("\nHere's another approach to the arithmetic quiz.\n")

def addition_quiz2():
    while True:
        response = input("What is 3 + 4? (Enter q to quit.) ")
        if response != 'q':
            response = int(response)
            continue
        if response == 7:
            break
        if response == 'q':
            break
    if response == 7:
        print("Correct!")

# print()

def report_classes_if_any():
# Recap from Week-10 overview
    classes = []
    if classes:
        print(classes)
    else:
        print("No classes taken\n")

def build_classes_maybe_math():
    classes = []
    for i in range(5):
        classes.append("CS Class")
    print(classes)
    # Run through the list and see if we find "Math Class".
    no_math = True
    for course in classes:
        if course == "Math Class":
            no_math = False
    if no_math:
        print("You're not taking math")
    else:
        print("You're taking math")
    # Run through the list and see if we find "Math Class".
    print("Classes are:")
    for i in range(len(classes)):
        print(classes[i])

# Invoke the function addition_quiz.
addition_quiz()