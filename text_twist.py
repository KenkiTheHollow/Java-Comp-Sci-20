import time

# ---------- LOAD DICTIONARY ----------
def load_dictionary():
    words = []
    file = open("dictionary.txt", "r")
    for line in file:
        words.append(line.strip())
    file.close()
    return words

# ---------- CAN MAKE METHOD ----------
def can_make(word, letters):
    letters_list = list(letters)

    for ch in word:
        if ch in letters_list:
            letters_list.remove(ch)
        else:
            return False

    return True

# ---------- MAIN PROGRAM ----------
def main():
    dictionary = load_dictionary()

    letters = input("Enter the 6 letters from Text Twist: ").lower()

    print("You have 5 seconds to switch to Text Twist...")
    time.sleep(5)

    for word in dictionary:
        if can_make(word, letters):
            print(word)

main()
