def main():
    print("Welcome to camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your\ndesert trek and out run the natives.")

    done = False
    while done == False:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            done = True

main()
