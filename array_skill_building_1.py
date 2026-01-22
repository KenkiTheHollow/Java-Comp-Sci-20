import random

SIZE = 100

# ---------- ARRAY METHODS ----------

def populate_random(arr):
    for i in range(SIZE):
        arr[i] = random.randint(1, 100)


def populate_sequential(arr):
    for i in range(SIZE):
        arr[i] = i + 1


def display(arr):
    for i in range(SIZE):
        print(arr[i], end=" ")
        if (i + 1) % 10 == 0:
            print()
    print()


def shuffle(arr):
    for i in range(SIZE):
        j = random.randint(0, SIZE - 1)
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


def find(arr, number):
    for i in range(SIZE):
        if arr[i] == number:
            return i
    return -1


def ascending(arr):
    for i in range(SIZE - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def shuffleSort(arr):
    attempts = 0
    while attempts < 10000:
        if ascending(arr):
            return True
        shuffle(arr)
        attempts += 1
    return False


def lowest(arr):
    low = arr[0]
    for i in range(1, SIZE):
        if arr[i] < low:
            low = arr[i]
    return low


def highest(arr):
    high = arr[0]
    for i in range(1, SIZE):
        if arr[i] > high:
            high = arr[i]
    return high


def count_occurrences(arr, number):
    count = 0
    for i in range(SIZE):
        if arr[i] == number:
            count += 1
    return count


def replace(arr, old, new):
    for i in range(SIZE):
        if arr[i] == old:
            arr[i] = new


def greatest_sum_10(arr):
    max_sum = 0
    max_index = 0

    for i in range(SIZE - 9):
        total = 0
        for j in range(10):
            total += arr[i + j]

        if total > max_sum:
            max_sum = total
            max_index = i

    print("Greatest sum of 10 consecutive values:", max_sum)
    print("Starting index:", max_index)


# ---------- MAIN PROGRAM ----------

def main():
    arr = [0] * SIZE
    running = True

    while running:
        print("\nMENU")
        print("0. Exit")
        print("1. Populate randomly")
        print("2. Populate sequentially (1–100)")
        print("3. Display array")
        print("4. Shuffle array")
        print("5. Find number")
        print("6. Check if ascending")
        print("7. Shuffle sort")
        print("8. Lowest value")
        print("9. Highest value")
        print("10. Count occurrences")
        print("11. Replace number")
        print("12. Greatest sum of 10 consecutive values")

        choice = int(input("Enter choice: "))

        if choice == 0:
            running = False

        elif choice == 1:
            populate_random(arr)

        elif choice == 2:
            populate_sequential(arr)

        elif choice == 3:
            display(arr)

        elif choice == 4:
            shuffle(arr)

        elif choice == 5:
            num = int(input("Enter number to find: "))
            index = find(arr, num)
            print("Index:", index)

        elif choice == 6:
            print("Ascending:", ascending(arr))

        elif choice == 7:
            result = shuffleSort(arr)
            print("Shuffle sort success:", result)

        elif choice == 8:
            print("Lowest value:", lowest(arr))

        elif choice == 9:
            print("Highest value:", highest(arr))

        elif choice == 10:
            num = int(input("Enter number to count: "))
            print("Occurrences:", count_occurrences(arr, num))

        elif choice == 11:
            old = int(input("Number to replace: "))
            new = int(input("Replace with: "))
            replace(arr, old, new)

        elif choice == 12:
            greatest_sum_10(arr)


main()
