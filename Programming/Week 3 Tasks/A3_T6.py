print("1. Length")
print("2. Weight")
print("3. Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print("1. Meters to kilometers")
    print("2. Kilometers to meters")

    length_choice = int(input("Your choice: "))

    if length_choice == 1:
        meters = float(input("Enter meters: "))
        kilometers = meters / 1000
        print(round(kilometers, 1), "kilometers")

    elif length_choice == 2:
        kilometers = float(input("Enter kilometers: "))
        meters = kilometers * 1000
        print(round(meters, 1), "meters")

    else:
        print("Unknown option.")

elif choice == 2:
    print("1. Grams to pounds")
    print("2. Pounds to grams")

    weight_choice = int(input("Your choice: "))

    if weight_choice == 1:
        grams = float(input("Enter grams: "))
        pounds = grams / 453.59237
        print(round(pounds, 1), "pounds")

    elif weight_choice == 2:
        pounds = float(input("Enter pounds: "))
        grams = pounds * 453.59237
        print(round(grams, 1), "grams")

    else:
        print("Unknown option.")

elif choice == 3:
    print("Exiting...")

else:
    print("Unknown option.")