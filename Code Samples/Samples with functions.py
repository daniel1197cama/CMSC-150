def hello_name(user_name):
    print("Hello " + user_name)

hello_name("Daniel")


def f_to_c(farenheit):
    celsius = (farenheit - 32) * 5 / 9
    return celsius

celsius = f_to_c(100)
print(celsius)
celsius = f_to_c(23)
print(celsius)

user_input = int(input("please enter a number: "))
if user_input > 0:
    print("Positive")
elif user_input == 0:
    print("Saved by zero")
else:
    print("negative")

user_input = int(input("please enter a number: "))
if user_input >= -10 and  user_input <= 10:
    print("success")