# A function that calls itself is a recursive function.
# Recursion is way to produce repetition in programming.
def maze2():
    """Plays a maze game in a recursive implementation."""
    # INITIALIZE the variable response and subsequently UPDATE it.
    response = input(
        "You are lost in a scary maze. Will you go left or right? ")
    # DEFINE A STOP CONDITION.
    if response != "left":
        print("You fall in a pit. You lose.")
    else:
        # HAVE THE FUNCTION CALL ITSELF.
        maze2()  # recursive call: The function calls itself.


# This function gets into an infinite loop.
def countdown_recursive(number):
    print(number)
    countdown_recursive(number - 1)


def countdown_recursive2(number):
    if number < 0:
        print("Blastoff!")
    else:
        print(number)
        countdown_recursive2(number - 1)


# This function gets into an infinite loop.
def countdown_recursive3(number):
    if number < 0:
        print("Blastoff!")
    print(number)
    countdown_recursive(number - 1)


# This function gets into an infinite loop.
def countdown_recursive4(number):
    print(number)
    countdown_recursive4(number - 1)
    if number < 0:
        print("Blastoff!")


def countdown_recursive_go(number):
    """Count down from number to 0 with recursion, using a 'go' condition."""
    if number >= 0:
        print(number)
        countdown_recursive_go(number - 1)
    else:
        print("Blastoff!")


# maze2()
countdown_recursive_go(3)
