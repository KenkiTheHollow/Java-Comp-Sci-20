import random

# 1. Instantiate a 20x20 array
grid = []
for i in range(20):
    row = []
    for j in range(20):
        row.append(0)
    grid.append(row)

# 2. Populate the array with random numbers (1-100 for example)
for i in range(20):
    for j in range(20):
        grid[i][j] = random.randint(1, 100)

# 3. Display the array in a neat grid
print("20x20 Grid:")
for row in grid:
    for num in row:
        print(f"{num:3}", end=" ")  # format for spacing
    print()

# 4. Find the 3x3 box with the greatest sum
max_sum = -1
top_left_x = 0
top_left_y = 0

for i in range(20 - 2):  # row start index for 3x3 box
    for j in range(20 - 2):  # col start index for 3x3 box
        current_sum = 0
        for x in range(3):
            for y in range(3):
                current_sum += grid[i + x][j + y]
        if current_sum > max_sum:
            max_sum = current_sum
            top_left_x = i
            top_left_y = j

print(f"\nTop-left corner of 3x3 box with greatest sum: ({top_left_x}, {top_left_y})")
print(f"Sum of that box: {max_sum}")
