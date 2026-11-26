LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def writeFile(Filename, Content):
    file = open(Filename, "w")
    file.write(Content)
    file.close()


def askRows():
    rows = ""
    while True:
        row = input("Enter text: ")
        if row == "":
            break
        rows += row + "\n"
    return rows


def shiftCharacter(Character, Alphabets, Shift=13):
    if Character not in Alphabets:
        return Character
    return Alphabets[(Alphabets.index(Character) + Shift) % len(Alphabets)]


def rot13(Content):
    result = ""
    for character in Content:
        character = shiftCharacter(character, LOWER)
        character = shiftCharacter(character, UPPER)
        result += character
    return result


def main():
    text = askRows()
    ciphered = rot13(text)
    print(ciphered)
    filename = input("Enter filename to save: ")
    if filename == "":
        print("No filename given, text was not saved.")
    else:
        writeFile(filename, ciphered)
        print("Saved to", filename)


main()
