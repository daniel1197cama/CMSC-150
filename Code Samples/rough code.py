'''
import random

my_list = []
for i in range(1,100):
    my_list.append(random.randrange(1, 1001))

print(my_list)

total = 0
for item in my_list:
    total += item

print(total)

smallest_number = my_list[0]
for item in my_list:
    if item < smallest_number:
        smallest_number = item
print(smallest_number)
'''

# ord() function, letter to a number
# chr() function, number to a letter
'''
plain_text = "This is a test. ABCDEF"
for character in plain_text:
    x = ord(character)
    x + 1
    print(chr(x), end=" ")

encrypted_text = "Uijt!jt!b!uftu/!BCDEFG"
print()
for character in encrypted_text:
    x = ord(character)
    x -=2
    print(chr(x), end=" ")
'''
"""
#0
room = [ 1, None, None, None]
room_list.append(room)

#1
room = [ 2, None, None, None]
room_list.append(room)

#2
room = [ 3, None, None, None]
room_list.append(room)

#3
room = [None, None, 2, None]
room_list.append(room)

#4
room = [None, None, None, 2]
room_list.append(room)
"""
'''
name = "Link"
sex = "Male"
max_hit_points = 50
current_hit_points = 50
max_speed = 10

def d
'''
"""
class Character():
    ### This is a class that represents the main character in a game ###
    def __init__(self): # init stands for initialized
        self.name = "Link"
        self.sex = "Male"
        self.max_hit_points = 50
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10

class Adress():
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

home_address = Adress()
home_address.name = "John Smith"
home_address.line1 = " 701 N. C Street"
home_address.line2 = "Carver Science Building"
home_address.city =  "Indianola"
home_address.state = "IA"
home_address.zip = "50125"
"""
class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print("woof says " + self.name + ".")

dog_information = Dog()
dog_information.name = 2
dog_information.age = "Willi"
dog_information.weight = 15

dog_information.bark()