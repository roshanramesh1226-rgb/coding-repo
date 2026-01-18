# Simple Number Guessing Game in Python

import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")

    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__