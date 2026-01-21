# Class to mimic Java methods
class MethodPractice:

    @staticmethod
    def is_even(num):
        """Return True if num is even, False otherwise."""
        return num % 2 == 0

    @staticmethod
    def generate_greeting(name):
        """Return a greeting message for the given name."""
        return f"Hello, {name}!"

    @staticmethod
    def calculate_factorial(n):
        """Return the factorial of n using recursion."""
        if n < 0:
            return "Error: Factorial not defined for negative numbers"
        if n == 0 or n == 1:
            return 1
        return n * MethodPractice.calculate_factorial(n - 1)


# Main program
def main():
    # Sample inputs
    while True:
        try:
            number = int(input("Enter an integer to check if it is even: "))
            break
        except ValueError:
            print("Invalid input. Enter an integer.")

    name = input("Enter your name for a greeting: ")

    while True:
        try:
            n = int(input("Enter a non-negative integer for factorial: "))
            if n < 0:
                print("Number must be non-negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a non-negative integer.")

    # Call methods and display results
    print(f"\nIs {number} even? {MethodPractice.is_even(number)}")
    print(MethodPractice.generate_greeting(name))
    print(f"{n}! = {MethodPractice.calculate_factorial(n)}")


# Run the program
if __name__ == "__main__":
    main()
