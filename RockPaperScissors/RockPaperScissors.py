# Basic rock paper scissors game
# Author: Ryan Pitman

from random import randrange

# Store potential game results
results = ["rock", "paper", "scissors"]

# Initialize game
print("Rock paper scissors game!\n")

# Basic input loop for error checking
while True:
    userChoice = input("Input your choice to play: ").lower()

    # If input not within results array, repeat
    if userChoice == results[0] or userChoice == results[1] or userChoice == results[2]:
        break
    else:
        print("Invalid choice, try again!")

# Generate computer result
compuChoice = results[randrange(0, 3)]

# Results checking
if userChoice == compuChoice:   # If choices are same, result is tie
    print(f"Its a tie! You both chose {compuChoice}")
elif userChoice == results[0]:  # If user chooses rock
    if compuChoice == results[1]:   # Computer chooses paper, user loses
        print(f"You lose! The computer chose {compuChoice}")
    else:   # User wins
        print(f"You win! The computer chose {compuChoice}")
elif userChoice == results[1]:  # If user chose paper
    if compuChoice == results[2]: # Computer chooses scissors, user loses
        print(f"You lose! The computer chose {compuChoice}")
    else:   # User wins
        print(f"You win! The computer chose {compuChoice}")
else:   # Last possibility is user chose scissors
    if compuChoice == results[0]:   # Computer chose rock, user loses
        print(f"You lose! The computer chose {compuChoice}")
    else:   # User wins
        print(f"You win! The computer chose {compuChoice}")
