def input_in_range(a, b):
    """
    Prompts the user to enter an integer between a and b (inclusive).
    Repeats until a valid number is entered.
    """
    low = min(a, b)
    high = max(a, b)

    while True:
        try:
            n = int(input(f"Please enter a number from {low} to {high}: "))
            if low <= n <= high:
                return n
            else:
                print("That is not a valid input.")
        except ValueError:
            print("That is not a valid input.")


# Example usage
result = input_in_range(1, 10)
print("You entered:", result)
