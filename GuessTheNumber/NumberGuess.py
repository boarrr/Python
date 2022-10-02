from random import randrange

userDiff = None
numToGuess = 0
guesses = 3

print(f"Guess the number within {guesses} attempts to win!")

while True:
    userDiff = input("Would you like [1] Easy, [2] Medium or [3] Hard?: ")

    if userDiff == '1' or userDiff == '2' or userDiff == '3':
        userDiff = 30 * int(userDiff)
        break
    else:
        print("Invalid input, try again!")


print(f"Guess the number between 1 and {userDiff}")
numToGuess = randrange(userDiff)

while guesses != 0:
    while True:
        try:
            userGuess = int(input("Guess a number: "))
            break
        except ValueError:
            print("Input is not a number, try again!")

    if userGuess == numToGuess:
        print(f"You have won! The number was {numToGuess}!")
        break
    else:
        if userGuess > numToGuess:
            print("Your number was too high!")
        else:
            print("Your number was too low!")
        guesses -= 1

if guesses == 0:
    print(f"You failed! The number was {numToGuess}")

