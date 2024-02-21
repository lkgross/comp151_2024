family = ["Donald", "Mercedes", "Chandra", "Suzanne"]
print("The family members are:")
for member in family:
    print(member)
print("There are four members.")  # The for loop is no longer being used.

print()

print("The family members are:")
for member in family:
    print(member)
    print("is one member.")  # The for loop is still being used.
print("There are four members.")  # The for loop is still being used.

print()
for number in range(11):
    print(number)

print()

for i in range(11):
    print(i)

print()

# Print "Hello!" eleven times
for number in range(11):
    print("Hello!")

# The function range starts a sequence from 0 by default.
# We saw range(11) is a sequence of 11 numbers that starts from 0
# and goes up to and including 10.
# The function range can also take another starting value other than 0.
for number in range(1, 11):
    print(number)

print()

for number in range(1, 11, 2):
    print(number)

print()

# Another to print 1 to 10 inclusive.
for i in range(10):
    print(i + 1)

print()

# Another way to print 1, 3, 5, 7, 9.
for i in range(5):
    print(1 + 2 * i)

print()

for number in range(1, 11, 2):
    print(number**2)

print()

# List comprehension
values = [number**2 for number in range(1, 11, 2)]
print(values)

print()

# Loop through a list index-by-index.

for i in range(len(family)):
    print(family[i])

print()

prizes = ['cupcake', 'cash', 'house']
values = [2.0, 200, 200_000]

# for prize in prizes:

for i in range(len(prizes)):
    print(f"The prize {prizes[i]} is worth ${values[i]}.")

print()

comments = []
for i in range(len(prizes)):
    comments.append(f"The prize {prizes[i]} is worth ${values[i]}.")

print(comments)