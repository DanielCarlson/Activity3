choice = "y"
points = 0
while choice.lower() != "n":
    points = int(input("Enter total number of points earned: "))
    while points > 1000 or points < 0:
        print("Number of points must be between 0 and 1000. Please try again.")
        points = int(input("Enter total number of points earned: "))
    if points >= 0 and points <600:
        print("Letter grade: F")
    elif points >= 600 and points < 700:
        print("Letter grade: D")
    elif points >= 700 and points < 780:
        print("Letter grade: C")
    elif points >= 780 and points < 820:
        print("Letter grade: C+")
    elif points >= 820 and points < 880:
        print("Letter grade: B")
    elif points >= 880 and points < 920:
        print("Letter grade: B+")
    elif points >= 920 and points <=1000:
        print("Letter grade: A")
    choice = input("\nContinue (y/n)?: ")
    print(choice)
    while choice != "y" and choice != "n":
        print("Answer must be y or n. Please try again.")
        choice = input("\nContinue (y/n)?: ")
print("Bye")