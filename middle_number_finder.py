def middle(a, b, c):
    """Return the middle value of three integers, handling repeats correctly."""
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c


# Main program
while True:
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        c = int(input("Enter the third integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

print("The middle value is:", middle(a, b, c))
