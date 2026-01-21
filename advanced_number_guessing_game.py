import random

score_wins = 0
score_losses = 0
play_again = "y"

while play_again == "y":

    print("\nWelcome to the Number Guessing Game")
    print("===================================")
    print("Choose a difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-20)")
    print("3. Hard (1-50)")

    difficulty = input("Enter 1, 2, or 3: ")

    if not difficulty.isdigit():
        print("Invalid choice. Defaulting to Easy.")
        max_num = 10
    else:
        difficulty = int(difficulty)
    
        if difficulty == 1:
            max_num = 10
        elif difficulty == 2:
            max_num = 20
        elif difficulty == 3:
            max_num = 50
        else:
            print("Invalid choice. Defaulting to Easy.")
            max_num = 10

    target = random.randint(1, max_num)
    guesses = 0
    max_guesses = 3
    win = False

    while guesses < max_guesses:
        guess = input(f"Guess a number (1-{max_num}): ")

        # Error trapping (numeric + range check)
        if not guess.isdigit():
            print("Invalid input. Enter a number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > max_num:
            print("Number out of range.")
            continue

        guesses += 1

        if guess == target:
            print("You got it!")
            win = True
            score_wins += 1
            break
        else:
            diff = abs(guess - target)

            if diff <= 2:
                print("Hot!")
            elif diff <= 5:
                print("Warm!")
            else:
                print("Cold!")

            if guesses < max_guesses:
                print("Try again...")

    if not win:
        print("You lose!")
        print("The correct number was:", target)
        score_losses += 1

    print(f"Score: {score_wins} wins, {score_losses} losses")
    play_again = input("Play again? (y/n): ").lower()
