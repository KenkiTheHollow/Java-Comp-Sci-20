def roman_numeral(n):
    """Convert a number from 1 to 100 into Roman numerals using only basic Python constructs."""
    result = ""

    # Tens place
    while n >= 100:
        result += "C"
        n -= 100
    if n >= 90:
        result += "XC"
        n -= 90
    if n >= 50:
        result += "L"
        n -= 50
    if n >= 40:
        result += "XL"
        n -= 40
    while n >= 10:
        result += "X"
        n -= 10

    # Ones place
    if n == 9:
        result += "IX"
        n -= 9
    if n >= 5:
        result += "V"
        n -= 5
    if n == 4:
        result += "IV"
        n -= 4
    while n >= 1:
        result += "I"
        n -= 1

    return result


# Main program with input error trapping
while True:
    try:
        number = int(input("Enter a number from 1 to 100: "))
        if 1 <= number <= 100:
            break
        else:
            print("Number must be between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Roman numeral:", roman_numeral(number))
