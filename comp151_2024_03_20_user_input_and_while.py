# You can prompt a user for input.
# Use the input function.
# The user's input is initially stored as a string.

name = input("What is your name? ")
print(f"Hello, {name}!")

age = input("How old are you? ")
# I want to treat age as numerical information.
age = int(age)
if age >= 18:
    print("You can vote!")
elif age >= 10 and age <= 12:
    print("You can be in the 10-12-year-old book group.")

print()

tip = float(input("How much tip? "))
if tip < 2:
    print("That's kind of low.")

print()

print("You are lost in a scary maze.")
# RESPONSE IS GIVEN AN INITIAL VALUE
# to prevent an error when the condition
# for the while loop is first evaluated.
response = input("Will you go left or right? ")
# The loop condition has one variable: response
while response == "left":
    # LOOP VARIABLE(S) MUST BE UPDATED IN THE
    # BODY OF THE WHILE LOOP!
    # This avoids an infinite loop.
    response = input("Will you go left or right? ")
print("You fall in a pit. You lose.")