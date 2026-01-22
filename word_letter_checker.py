# ---------------------------
# Function to check if word can be made from letters
# ---------------------------
def check_letters(word, letters):
    letters_list = list(letters)  # convert the letters string to a list

    for char in word:
        if char in letters_list:
            letters_list.remove(char)  # remove the letter once used
        else:
            return False  # letter not available
    return True

# ---------------------------
# Main program
# ---------------------------
word = input("Enter the word to check: ")
letters = input("Enter the available letters: ")

if check_letters(word, letters):
    print("TRUE")
else:
    print("FALSE")
