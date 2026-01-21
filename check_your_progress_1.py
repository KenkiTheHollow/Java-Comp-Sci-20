# Read inputs
m = int(input())
f1 = int(input())
f2 = int(input())

# Check for zero inputs
if f1 == 0 or f2 == 0:
    print("Error")
else:
    # Loop through numbers from 1 to m
    for num in range(1, m + 1):
        # Check if divisible by both f1 and f2
        if num % f1 == 0 and num % f2 == 0:
            print(num)
