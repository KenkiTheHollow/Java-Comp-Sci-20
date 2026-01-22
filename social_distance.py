# ---------------------------
# 1. Input seats
# ---------------------------
n = int(input("How many seats are there? "))
seats = []

for i in range(n):
    while True:
        try:
            occupied = int(input(f"Is seat {i+1} occupied (1 = yes, 0 = no)? "))
            if occupied in [0, 1]:
                seats.append(occupied)
                break
            else:
                print("Enter 1 for yes or 0 for no.")
        except ValueError:
            print("Enter a valid integer (1 or 0).")

# ---------------------------
# 2. Calculate desirability
# ---------------------------
# Initialize desirability: higher value = more desirable
desirability = [0] * n

for i in range(n):
    if seats[i] == 1:
        # seat is occupied, reduce desirability of nearby seats
        for j in range(n):
            if i != j:
                distance = abs(i - j)
                # seats closer get lower desirability
                desirability[j] += distance
    else:
        # unoccupied seat, start with distance 0
        desirability[i] += 0

# ---------------------------
# 3. Find best seat
# ---------------------------
max_value = -1
best_seat = -1

for i in range(n):
    if seats[i] == 0:  # only consider empty seats
        if desirability[i] > max_value:
            max_value = desirability[i]
            best_seat = i
        # tie-breaker: seat closer to ends
        elif desirability[i] == max_value:
            if i < best_seat:  # closer to the start
                best_seat = i

# ---------------------------
# 4. Display results
# ---------------------------
print(" ".join(str(s) for s in seats))
print(f"The next person should sit in seat: {best_seat + 1}")
