import itertools

# ---------------------------
# Generate all solutions
# ---------------------------
def generate_solutions():
    """Generate all 4096 possible 4-peg patterns using numbers 1-8."""
    colors = [1,2,3,4,5,6,7,8]
    return list(itertools.product(colors, repeat=4))

# ---------------------------
# Compare guess to solution
# ---------------------------
def feedback(guess, solution):
    """Return (correct_place, correct_color_wrong_place)"""
    correct_place = sum(g==s for g,s in zip(guess, solution))
    # Count colors in wrong place
    guess_counts = [0]*9
    solution_counts = [0]*9
    for g,s in zip(guess, solution):
        if g != s:
            guess_counts[g] += 1
            solution_counts[s] += 1
    correct_color_wrong_place = sum(min(guess_counts[i], solution_counts[i]) for i in range(1,9))
    return correct_place, correct_color_wrong_place

# ---------------------------
# Mastermind Assistant
# ---------------------------
def mastermind_assistant():
    solution_set = generate_solutions()
    possible = [True]*4096
    
    print("Think of a 4-peg pattern using numbers 1-8 (pegs can repeat).")
    
    while True:
        # Find first possible guess
        guess_index = possible.index(True)
        guess = solution_set[guess_index]
        print("My guess is:", guess)
        
        # Get feedback from user
        correct = int(input("How many were correct? "))
        wrong_place = int(input("How many were out of place? "))
        
        if correct == 4:
            print("I found your solution!")
            break
        
        # Eliminate this guess
        possible[guess_index] = False
        
        # Filter remaining possible solutions
        for i, sol in enumerate(solution_set):
            if possible[i]:
                f = feedback(guess, sol)
                if f != (correct, wrong_place):
                    possible[i] = False

# ---------------------------
# Run Assistant
# ---------------------------
mastermind_assistant()
