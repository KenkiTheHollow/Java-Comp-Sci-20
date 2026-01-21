# Read four depth readings from the user
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

# Check for strictly increasing sequence
if d1 < d2 < d3 < d4:
    print("Fish Rising")
# Check for strictly decreasing sequence
elif d1 > d2 > d3 > d4:
    print("Fish Diving")
# Check for all identical readings
elif d1 == d2 == d3 == d4:
    print("Fish At Constant Depth")
# Anything else is random noise / no fish
else:
    print("No Fish")
