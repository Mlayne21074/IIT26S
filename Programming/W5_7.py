DELIMITER = ","


def collectWords():
    words = ""
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words += word + DELIMITER
    return words


def analyseWords(words):
    wordList = words.split(DELIMITER)[:-1]
    wordCount = len(wordList)
    charCount = len("".join(wordList))
    average = charCount / wordCount if wordCount else 0
    print("Words:", wordCount)
    print("Characters:", charCount)
    print(f"Average word length: {average:.2f}")


def main():
    words = collectWords()
    analyseWords(words)


main()
