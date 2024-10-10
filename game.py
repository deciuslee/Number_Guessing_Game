# Jonathan Lee
# Purpose: Number Guessing Game

# Randomly choose a number between 1 and 100 (inclusive)
# Have the player enter a guess via input
# Tell the player the guess is high, low, or correct
# If high or low, allow the player to enter another guess
# Give the player an option to quit at any time
# Reward the player for a correct guess (ex., "Good job!")
# Tell the player how many guesses it took to guess correctly


# import random number generator
import random

# generate random number between 1 and 100, inclusive
number = random.randint(1, 100)
attempts = 0

print(f"*****Number Guessing Game*****")
print()

print(f"Hi there! I'm thinking of a number between 1 and 100. Can you guess it?")

# create loop to count the number of attempts
while True:
    try:
        guess = input("Please enter your guess or Press 'q' to quit:")
        attempts += 1
        if guess.lower() == "q":
            print(f"Thanks for playing.")
            break

        guess = int(guess)

        if guess < number:
            print("Guess is too low! Please try again.")
        elif guess > number:
            print("Guess is too high! Please try again.")
        else:
            print(f"Congratulations, your guess is correct!")
            print(f"It took you {attempts} attempts.")
            print("Thanks for playing.")
            exit()


    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")