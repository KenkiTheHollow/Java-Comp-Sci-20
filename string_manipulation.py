def get_length(st):
    count = 0
    for _ in st:
        count += 1
    return count

def letter_count(st, ch):
    count = 0
    for c in st:
        if c == ch:
            count += 1
    return count

def reverse(st):
    rev = ""
    for i in range(len(st)-1, -1, -1):
        rev += st[i]
    return rev

def is_anagram(st1, st2):
    if get_length(st1) != get_length(st2):
        return False
    arr1 = list(st1)
    arr2 = list(st2)
    for c in arr1:
        if c in arr2:
            arr2.remove(c)
        else:
            return False
    return True

def pig_latin(st):
    if get_length(st) == 0:
        return ""
    return st[1:] + st[0] + "ay"

def remove_duplicates(st):
    result = ""
    seen = []
    for c in st:
        if c not in seen:
            result += c
            seen.append(c)
    return result

def compression(st):
    if get_length(st) == 0:
        return ""
    result = st[0] + " "
    current = st[0]
    count = 1
    output = []
    for i in range(1, get_length(st)):
        if st[i] == current:
            count += 1
        else:
            output.append(str(count))
            current = st[i]
            count = 1
    output.append(str(count))
    return result + " ".join(output)


# ------------------------
# Main interactive program
# ------------------------
print("String Manipulation Methods:")
print("1: Get Length")
print("2: Letter Count")
print("3: Reverse String")
print("4: Check Anagram")
print("5: Pig Latin")
print("6: Remove Duplicates")
print("7: Compression")

while True:
    try:
        choice = int(input("Enter the number of the method you want to run (1-7): "))
        if 1 <= choice <= 7:
            break
        else:
            print("Invalid choice. Enter a number from 1 to 7.")
    except ValueError:
        print("Invalid input. Enter a number.")

# Get input based on method
if choice == 1:
    st = input("Enter a string: ")
    print("Length:", get_length(st))
elif choice == 2:
    st = input("Enter a string: ")
    ch = input("Enter a character: ")
    print("Letter count:", letter_count(st, ch))
elif choice == 3:
    st = input("Enter a string: ")
    print("Reversed:", reverse(st))
elif choice == 4:
    st1 = input("Enter first string: ")
    st2 = input("Enter second string: ")
    print("Anagram test:", is_anagram(st1, st2))
elif choice == 5:
    st = input("Enter a word: ")
    print("Pig Latin:", pig_latin(st))
elif choice == 6:
    st = input("Enter a string: ")
    print("Remove duplicates:", remove_duplicates(st))
elif choice == 7:
    st = input("Enter a string of 1s and 0s: ")
    print("Compression:", compression(st))
