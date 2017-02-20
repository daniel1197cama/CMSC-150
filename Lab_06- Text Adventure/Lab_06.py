"""
This is a text adventure game that takes you around the world to the "Seven Wonders of the World". You put on a
set of VR headset and jump from a virtual room to another virtual room to explore the world.
"""
# Room descriptions
room_list = []
room = ["This is were everything starts. Make sure you have your headset on. You see two doors: "
        "\none to your left and the other down the room. Have fun!", None, None, 5, 1]
room_list.append(room)
room = ["You are in the Great Wall of China! It was built over 2,000 years ago to "
        "\nto protect the borders of the Chinese Empire from invading Mongols.", None, 0, 4, 2]
room_list.append(room)
room = ["You are in the Christ the Redeemer Statue in Rio the Janeiro, Brazil!"
        "\nIt took 9 years from 1922 to 1931 to construct the statue.It measures 124 ft tall!", None, 1, 3, None]
room_list.append(room)
room = ["You are in Machu Picchu, Peru! Up in the Andean peaks, Machu Picchu used to be an Incan city in the mid-1400s."
        "\nThe site can only be reached by foot, train or helicopter. You see three different doors", 2, 4, 6, None]
room_list.append(room)
room = ["You are in the Chichen Itza in the Yucatan Peninsula, Mexico! This is a powerful city created by the Mayan"
        "\ncivilization as a trading center for cloth, slaves,honey and salt. The Mayas flourished from approx. "
        "\n800 to 1200 D.C. and were known for having a sophisticated astronomical observatory. "
        "You see four different doors around you.", 1, 5, 7, 3]
room_list.append(room)
room = ["You are in the Roman Colosseum in Rome! The Colosseum was built between 70 and 80 A.D. and was in use for "
        "some 500 years. \nNearly 50,00 spectators gathered to watch gladiators, animal hunts, and "
        "executions. You see two doors; one will take you to the beginning and the other to a wonderful place! ",
        0, None, None, 4]
room_list.append(room)
room = ["Your are in the Taj Majal in India! It was built between 1631 and 1653 dedicated for the wife of "
        "Emperor Shah Jahan. \nMore than 1,00 elephants were used to transport the construction materials."
        "\nYour VR headset shows 2 different doors, to your right and straight up.", 3, 7, None, None]
room_list.append(room)
room = ["You are Petra Jordan! Petra was the capital of the Nabataean Empire. They existed form ( B.C. to 40 A.D."
        "\nThis civilization manipulated water technology, constructed tunnels and water chambers.  "
        "\nYour VR experience is almost coming to an end. You can see three doors but one of them will take you to an "
        "additional place on earth", 4, 8, None, 6]
room_list.append(room)
room = ["You are in the Great Pyramid of Giza in Egypt! This pyramid is one of the Seven Wonders of the Ancient World "
        "and it is a marvel of human engineering and construction. \nThis Pyramid was built between 2589 and 2504 B.C."
        " Isn't amazing!\nYou have come to the end of this wonderful journey proceed to your right and we hope to see "
        "you again soon! ", None, 9, None, 7]
room_list.append(room)
room = ["This world is so beautiful and we are glad that you took the time to explore it through the VR experience!"
        "\nPlease enter the command 'QUIT' to take your VR headset off.", None, None, None, None]
room_list.append(room)

current_room = 0
# Instructions
print('You are in a virtual reality museum that lets you travel to the most iconic places on earth,')
print('"The Seven Wonders of the World". Enter one of the following commands and enjoy the pleasure of')
print('a VR experience by going places:')
print("- UP")
print("- DOWN")
print("- LEFT")
print("- RIGHT")
print("- QUIT")

done = False
while not done:
    print()
    print(room_list[current_room][0])
    user_input = input("Where do you want to go now?: ")

    if user_input.upper() == "QUIT" or user_input.upper() == "Q":
        done = True

    elif user_input.upper() == "UP" or user_input.upper() == "U":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    elif user_input.upper() == "RIGHT" or user_input.upper() == "R":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    elif user_input.upper() == "DOWN" or user_input.upper() == "D":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    elif user_input.upper() == "LEFT" or user_input.upper() == "L":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    else:
        print("I don't understand what you typed.")
