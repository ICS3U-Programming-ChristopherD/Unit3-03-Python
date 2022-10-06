#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Oct. 5, 2022
# This program checks if the user guessed a number correctly
# using an If.. Then.. Else statement.

import random


def main():

    # Assigns a random number from 0-9 to the secret_number variable.
    secret_number = random.randint(0, 9)

    # Requests the user's guess.
    print("The secret number is within the range of 0-9")
    user_guess = float(input("Enter your guess: "))

    # Code executed if the user guessed correctly.
    if secret_number == user_guess:
        print("You guessed correctly!")

    # Code executed if the user guessed incorrectly.
    else:
        print(f"You guessed incorrectly. The correct answer was {secret_number}")


if __name__ == "__main__":
    main()
