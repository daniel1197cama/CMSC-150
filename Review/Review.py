""""
# Write a function called "f" that will pass all the tests below:
def f(x,y):
    f = x + y
    return f

# --- Tests. Do not change anything below this line. ---
# Write your code above the line to pass all the tests.

if f(30, 40) == 70:
    print("Test 1 passed")
else:
    print("Test 1 failed")

if f(0, 0) == 0:
    print("Test 2 passed")
else:
    print("Test 2 failed")

if f(-20, 10) == -10:
    print("Test 3 passed")
else:
    print("Test 3 failed")

if f(0.5, 0.5) == -10:
    print("Test 4 passed")
else:
    print("Test 4 failed")


# Write a function called "f" that will pass all the tests below:
def f(x,y):
    f = x * y
    return f
# --- Tests. Do not change anything below this line. ---
# Write your code above the line to pass all the tests.

if f(0, 0) == 0:
    print("Test 1 passed")
else:
    print("Test 1 failed")

if f(5, 0) == 0:
    print("Test 2 passed")
else:
    print("Test 2 failed")

if f(10, 10) == 100:
    print("Test 3 passed")
else:
    print("Test 3 failed")

if f(0.5, 0.5) == 0.25:
    print("Test 4 passed")
else:
    print("Test 4 failed")

# Write a function called "f" that will pass all the tests below:
def f(x, y, z):
    f = (x + y)/ z
    return f

# --- Tests. Do not change anything below this line. ---
# Write your code above the line to pass all the tests.

if f(10, 10, 1) == 20:
    print("Test 1 passed")
else:
    print("Test 1 failed")

if f(15, 10, 1) == 25:
    print("Test 2 passed")
else:
    print("Test 2 failed")

if f(10, 10, 2) == 10:
    print("Test 3 passed")
else:
    print("Test 3 failed")

if f(10, 10, 10) == 2:
    print("Test 4 passed")
else:
    print("Test 4 failed")

if f(4, 6, 2) == 5:
    print("Test 5 passed")
else:
    print("Test 5 failed")

if f(150, 50, 50) == 4:
    print("Test 6 passed")
else:
    print("Test 6 failed")

# Write a function called how_is_the_temperature that returns a string based
# on the temperature passed into it.
def how_is_the_temperature(x):
    if x == 95:
        return "Hot"
    elif x == 85:
        return "Warm"
    elif x == 70:
        return "Great"
    elif x == 50:
        return "Cool"

# --- Tests. Do not change anything below this line. ---
# Write your code above the line to pass all the tests.

if how_is_the_temperature(95) == "Hot":
    print("Test 1 passed")
else:
    print("Test 1 failed")

if how_is_the_temperature(85) == "Warm":
    print("Test 2 passed")
else:
    print("Test 2 failed")

if how_is_the_temperature(70) == "Great":
    print("Test 3 passed")
else:
    print("Test 3 failed")

if how_is_the_temperature(50) == "Cool":
    print("Test 4 passed")
else:
    print("Test 4 failed")

if how_is_the_temperature(50) == "Cold":
    print("Test 5 passed")
else:
    print("Test 5 failed")
"""
