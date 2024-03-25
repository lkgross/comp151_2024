response = 0
not_quit = True
while not(response == 7) and not_quit:
    response = input("What is 3 + 4? (Enter q to quit.) ")
    if response != 'q':
        response = int(response)
    else:
        not_quit = False
if response == 7:
    print("Correct!")

print("\nHere's another approach to the arithmetic quiz.\n")

while True:
    response = input("What is 3 + 4? (Enter q to quit.) ")
    if response != 'q':
        response = int(response)

    if response == 7:
        break
    if response == 'q':
        break
if response == 7:
    print("Correct!")
