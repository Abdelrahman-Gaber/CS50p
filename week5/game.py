import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        print("Level must be a positive number!")

number = random.randint(1,n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            break

    except ValueError:
        print("Guess must be aa positive number!")