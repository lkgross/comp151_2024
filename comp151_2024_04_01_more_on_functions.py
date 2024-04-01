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
    """Print whether the player has more than the dealer's 19 or not."""
    if player_points > 19:
        print("The player has more points than the dealer.")
    else:
        print("The player does not have more points than the dealer.")


def yell(mascot):
    for i in range(3):
        print(f"Go!\nGo, {mascot}!")


def cheers():
    yell("Yankees!")
    print()
    yell("Bears!")


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
cheers()
