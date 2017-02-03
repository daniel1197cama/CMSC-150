import random

head_count = 0
tail_count = 0

for i in range(50):
    random_number = random.randrange(2)

    if random_number == 0:
        print("heads")
        head_count += 1
    else:
        print("tails")
        tail_count += 1

print("Heads", head_count)
print("Tails", tail_count)

for row in range(10):
    for column in range(row):
        print(".", end=" ")
    for column in range(10 - row):
            print(column, end=" ")
    print()

print()

for row in range(1, 10):
    for column in range(9 - row, 0, -1):
        print("*", end=" ")
    for column in range(1, row + 1):
        print(column, end=" ")

    for column in range(row - 1, 0, -1):\
        print(column, end=" ")

    print()

print()

for i in range(20):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)

