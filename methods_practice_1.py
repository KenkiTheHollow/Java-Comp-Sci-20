# MathOperations class equivalent in Python
class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# Main program
def main():
    # Prompt user for input with error trapping
    while True:
        try:
            a = int(input("Enter the first integer: "))
            b = int(input("Enter the second integer: "))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    # Call methods and display results
    print("Results of operations:")
    print(f"{a} + {b} = {MathOperations.add(a, b)}")
    print(f"{a} - {b} = {MathOperations.subtract(a, b)}")
    print(f"{a} * {b} = {MathOperations.multiply(a, b)}")
    print(f"{a} / {b} = {MathOperations.divide(a, b)}")


# Run the program
if __name__ == "__main__":
    main()
