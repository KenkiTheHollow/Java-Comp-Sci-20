import random

# Welcome message
print("Welcome to the Number Guessing Game")
print("===================================")

# Generate a random number from 1 to 10
target = random.randint(1, 10)

# Initialize number of guesses
guesses = 0
max_guesses = 3
guessed_correctly = False

# Loop until correct guess or max guesses reached
while guesses < max_guesses and not guessed_correctly:
    guess = int(input("Try to guess the number (1-10): "))
    guesses += 1
    if guess == target:
        print("You got it!")
        guessed_correctly = True
    else:
        if guesses < max_guesses:
            print("Sorry that's not right...")
        else:
            print("Sorry that's not right...")

# If the user didn't guess correctly after 3 tries
if not guessed_correctly:
    print("You lose!")

