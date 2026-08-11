import random

secret_number = random.randint(1, 100)

guess = int(input("Guess a number from 1 to 100: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Try again: "))

print("Congratulations! You guessed the number!")
