def is_valid(word):
    if len(word) < 3 or len(word) > 6:
        return False

    for ch in word:
        if ch < 'a' or ch > 'z':
            return False

    return True


def main():
    words = []  # array to store unique valid words

    file = open("CopyrightFreeText.txt", "r")

    for line in file:
        parts = line.lower().split()

        for word in parts:
            clean = ""
            for ch in word:
                if 'a' <= ch <= 'z':
                    clean += ch

            if is_valid(clean) and clean not in words:
                words.append(clean)

    file.close()

    out = open("dictionary.txt", "w")
    for word in words:
        out.write(word + "\n")
    out.close()

    print("Dictionary created.")


main()
