room_list = []
room = ["You are in the living room with two long sofas and marble floor.",None, None, 5, 1]
room_list.append(room)
room = ["You are in a beautiful hallway. It looks like someone is at home", None, 0, 4, 2]
room_list.append(room)
room = ["You are in the front yard", 0, 1, None, None]
room_list.append(room)
room = ["You are in the bathroom", None, 4, 6, None]
room_list.append(room)
room = ["You are in the center of the hallway", 1, 5, 7, 3]
room_list.append(room)
room = ["You are in your bedroom", 0, None, 8, 4]
room_list.append(room)
room = ["Your are in the dining room", 3, 7, None, None]
room_list.append(room)
room = ["You are down the hallway", 4, 8, 9, 6]
room_list.append(room)
room = ["You are in the kitchen", 5, None, None, 7]
room_list.append(room)
room = ["You are in the backyard",7, None, None, None]
room_list.append(room)

current_room = 0

print("NORTH")
print("SOUTH")
print("EAST")
print("WEST")

done = False
while not done:
    print()
    print(room_list[current_room][0])
    user_input = input("What do you want to do?: ")
    if user_input.upper() == "NORTH" or user_input.upper()== "N":
        next_room = room_list[current_room][1]

        if next_room == None:
            print("You can't go that way!")
        if next_room != None:
            current_room = next_room

    elif user_input.upper() == "EAST" or user_input.upper()== "E":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way!")
        if next_room != None:
            current_room = next_room

    elif user_input.upper() == "SOUTH" or user_input.upper()== "S":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way!")
        if next_room != None:
            current_room = next_room

    elif user_input.upper() == "WEST" or user_input.upper()== "W":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way!")
        if next_room != None:
            current_room = next_room






