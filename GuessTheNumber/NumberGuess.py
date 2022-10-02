# Basic number guessing game, where user guesses a number within 3 tries
# Author: Ryan Pitman

from random import randrange

# Variable Declarations
userDiff = None
numToGuess = 0
guesses = 3

# Initialize game
print(f"Guess the number within {guesses} attempts to win!")

# Get user input
while True:
    userDiff = input("Would you like [1] Easy, [2] Medium or [3] Hard?: ")

    if userDiff == '1' or userDiff == '2' or userDiff == '3':
        userDiff = 30 * int(userDiff)
        break
    else:
        print("Invalid input, try again!")

# Prompt for guess
print(f"Guess the number between 1 and {userDiff}")
numToGuess = randrange(userDiff)

# Guess loop
while guesses != 0:
    # User input for guess with exception handling
    while True:
        try:
            userGuess = int(input("Guess a number: "))
            break
        except ValueError:
            print("Input is not a number, try again!")

    # User guessed correctly
    if userGuess == numToGuess:
        print(f"You have won! The number was {numToGuess}!")
        break
    else:   # User guessed incorrectly
        if userGuess > numToGuess:
            print("Your number was too high!")
        else:
            print("Your number was too low!")
        guesses -= 1

# Display loss message
if guesses == 0:
    print(f"You failed! The number was {numToGuess}")

