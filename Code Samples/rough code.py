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


