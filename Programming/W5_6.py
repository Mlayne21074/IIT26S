def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    Choice = input("Your choice: ")

    if Choice.isnumeric():
        return int(Choice)
    else:
        print("Unknown option!")
        return -1


def main():
    print("Program starting.")

    Count = 0

    while True:
        showOptions()
        Choice = askChoice()

        if Choice == 1:
            print("Current count -", Count)
        elif Choice == 2:
            Count = Count + 1
            print("Current count -", Count)
        elif Choice == 3:
            Count = 0
            print("Count reset.")
        elif Choice == 0:
            print("Exiting program.")
            break
        elif Choice != -1:
            print("Unknown option!")

        print()

    print()
    print("Program ending.")


main()
