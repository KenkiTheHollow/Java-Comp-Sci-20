import random

def random_number(a, b):
    """Return a random integer between a and b inclusive."""
    low = min(a, b)
    high = max(a, b)
    return random.randint(low, high)


# Main program
while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

print(f"\n100 random numbers between {min(a,b)} and {max(a,b)}:")

for _ in range(100):
    r = random_number(a, b)
    print(r)
