# Function to generate all cyclic shifts of a string
def cyclic_shifts(s):
    shifts = []
    n = len(s)
    for i in range(n):
        shift = s[i:] + s[:i]  # move first i chars to the end
        shifts.append(shift)
    return shifts

# Main program
T = input("Enter the text T: ")
S = input("Enter the string S: ")

# Generate all cyclic shifts of S
shifts = cyclic_shifts(S)

# Check if any shift is in T
found = False
for shift in shifts:
    if shift in T:
        found = True
        break

if found:
    print("yes")
else:
    print("no")
