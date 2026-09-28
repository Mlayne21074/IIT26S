name = input("Enter your name: ")

while True:
    print("\nMenu:")
    print("1. Print the name backwards")
    print("2. Print the first character")
    print("3. Show the amount of characters in the name")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name_backwards = name[::-1]
        print(f'Your name backwards is "{name_backwards}"')
    elif choice == "2":
        if name:
            first_char = name[0]
            print(f'The first character in name "{name}" is "{first_char}"')
        else:
            print("The name is empty.")
    elif choice == "3":
        name_length = len(name)
        print(f'There are {name_length} characters in the name "{name}"')
    elif choice == "4":
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")