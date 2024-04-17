import random


def more_points():
    """Print whether the player has more points than the dealer or not."""
    player_points = 17
    dealer_points = 19
    if player_points > dealer_points:
        print("The player has more points than the dealer.")
    else:
        print("The player does not have more points than the dealer.")


# The function is defined with a parameter NAME player_points.
def more_points_than_dealer(player_points):
    """Print whether the player has more points than the dealer's 19 or not."""
    if player_points > 19:
        print("The player has more points than the dealer.")
    else:
        print("The player does not have more points than the dealer.")


def yell(mascot, repetitions):
    """Print a cheer for mascot, repetitions number of times."""
    for i in range(repetitions):
        print(f"Go!\nGo, {mascot}!")


def cheers():
    """Call yell several times."""
    yell("Yankees!", 1)
    print()
    yell("Bears!", 3)
    print()
    yell("Jumbos!", 3)


def more_points_than_dealer2(player_points, dealer_points):
    """Print whether the player has more points than the dealer."""
    if player_points > dealer_points:
        print("The player has more points than the dealer.")
    else:
        print("The player does not have more points than the dealer.")


def player_has_more(player_points, dealer_points):
    """Return whether player_points is greater than dealer_points."""
    return player_points > dealer_points


def pick_a_name(roster):
    # Variables are local to the function in which they are defined.
    index = random.randrange(len(roster))
    print(f"I pick {roster[index]}!")


def gpa(As, Bs, Cs, Ds, Fs):
    """Return the GPA for a person who earns As A grades, Bs B grades, Cs C grades
    Ds D grades and Fs F grades in classes that are all worth the same number of credits."""
    return (4.0 * As + 3.0 * Bs + 2.0 * Cs + 1.0 * Ds) / (
                As + Bs + Cs + Ds + Fs)
    # Once you return from a function, you've left the function!
    # This line will never execute:
    print("Good job!")


# print(gpa(2, 2, 1, 0, 0))
print(player_has_more(player_points=23, dealer_points=19))

# pick_a_name(["Nathan", "Jared", "Jack", "Luiz", "Alex"])
# print(index)
# The function is not actually saying anything yet.
# more_points()
# The function is called or invoked with the parameter VALUE 20.
# To call the function, Python passes the value 20 to
# the function more_points_than_dealer.
# The parameter player_points is assigned the value 20.
# more_points_than_dealer(20)
# more_points_than_dealer(22)
# more_points_than_dealer(17)
# yell("Pandas")
# cheers()

# more_points_than_dealer2(17, 19)
# cheers()
