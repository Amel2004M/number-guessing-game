import random

a = random.randint(0, 100)  # inclusive of both 0 and 100

try:
    b = int(input("Give a number between 0 and 100: "))
    if a == b:
        print("You won!")
    else:
        print("You lost. The number was", a)
except ValueError:
    print("You need to enter a valid whole number")