def sum_of_digits(num):
    """
    Returns the sum of the digits of an integer.
    Negative numbers are treated as positive.
    """
    num = abs(num)  # Ignore negative sign
    total = 0
    while num > 0:
        total += num % 10  # Add the last digit
        num //= 10         # Remove the last digit
    return total


# Main program
while True:
    try:
        n = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("The sum of digits is:", sum_of_digits(n))
