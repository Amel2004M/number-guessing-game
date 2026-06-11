import random

a = random.randint(0, 20)  # inclusive of both 0 and 100

print("Welcome to this guessing number game")
print("You have 5 chances to find the right number. Good luck!")

try:
    i = 0
    while i < 3:
        b = int(input("Give a number between 0 and 20: "))

        if a == b:
            print("You won!")
            break
        elif a < b:
            print("Too high!")
        else:
            print("Too low!")

        i += 1

        if i < 3:
            print("Try again!")

    if i == 3:
        print("You lost. The number was", a)

except ValueError:
    print("You need to give a number")