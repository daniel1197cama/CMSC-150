import random

# Start main loop
def main():
    # VARIABLES
    thirst = 0
    camel_tiredness = 0
    miles_traveled = 0
    natives_traveled = - 20
    drinks = 3

    # Game instructions
    print("Welcome to camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    done = False
    while not done:
        print("\nA. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            done = True

        # Status
        elif user_choice.upper() == "E":
            print("\nMiles traveled: ", miles_traveled)
            print("Drinks in canteen: ", drinks)
            print("The natives are ", (miles_traveled - natives_traveled), " miles behind you.")
        # Stop for the night
        elif user_choice.upper() == "D":
            camel_tiredness = 0
            print("\nYou have stopped for the night and your camel is happy")
            natives_traveled += random.randrange(7, 16)

        # Move full speed
        elif user_choice.upper() == "C":
            move = random.randrange(10, 21)
            miles_traveled += move
            print("\nMiles traveled: ", move)
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            natives_traveled += random.randrange(7, 15)
            if not done and random.randrange(1, 21) == 1:
                print("Wow you found an oasis.\nYour canteens are filled and you are no longer thirsty.")
                print("Your camel is also recharged!")
                thirst = 0
                drinks = 3
                camel_tiredness = 0

        # Move moderate speed
        elif user_choice.upper() == "B":
            move = random.randrange(5, 12)
            miles_traveled += move
            print("\nMiles traveled: ", move)
            thirst += 1
            camel_tiredness += 1
            natives_traveled += random.randrange(8, 16)
            if not done and random.randrange(1, 21) == 1:
                print("Wow you found an oasis.\nYour canteens are filled and you are no longer thirsty.")
                print("Your camel is also recharged!")
                thirst = 0
                drinks = 3
                camel_tiredness = 0

        # Drink from canteen
        elif user_choice.upper() == "A":
            natives_traveled += random.randrange(2, 5)
            print("\nThat was refreshing!")
            if drinks > 0:
                drinks -= 1
                thirst = 0
            else:
                print("\nThere are no drinks left")

        # Not done check
        if thirst > 6:
            print("You died of thirst!")
            done = True
        elif thirst > 4:
            print("You are thirsty")

        if camel_tiredness > 8:
            print("Your camel is dead.")
        elif camel_tiredness > 5:
            print("Your camel is getting tired")

        if natives_traveled >= miles_traveled:
            print("The natives have caught up to you. Game over!")
            done = True
        elif miles_traveled - natives_traveled < 15:
            print("The natives are getting close!")

        if miles_traveled >= 200:
            print("You have made it across the desert! You Win!")
            done = True
main()