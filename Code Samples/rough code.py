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
