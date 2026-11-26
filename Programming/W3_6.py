while True:
    print("\nMAIN MENU")
    print("1. Length")
    print("2. Weight")
    print("3. Exit")

    Choice = input("Choose an option: ")

    if Choice == "1":
        print("\nLENGTH MENU")
        print("1. Meters to kilometers")
        print("2. Kilometers to meters")

        Option = input("Choose an option: ")

        if Option == "1":
            Value = float(input("Enter meters: "))
            Result = Value * 0.001
            print("Result:", round(Result, 1), "kilometers")
        elif Option == "2":
            Value = float(input("Enter kilometers: "))
            Result = Value * 1000
            print("Result:", round(Result, 1), "meters")
        else:
            print("Unknown option.")

    elif Choice == "2":
        print("\nWEIGHT MENU")
        print("1. Grams to pounds")
        print("2. Pounds to grams")

        Option = input("Choose an option: ")

        if Option == "1":
            Value = float(input("Enter grams: "))
            Result = Value * 0.002205
            print("Result:", round(Result, 1), "pounds")
        elif Option == "2":
            Value = float(input("Enter pounds: "))
            Result = Value * 453.6
            print("Result:", round(Result, 1), "grams")
        else:
            print("Unknown option.")

    elif Choice == "3":
        print("Exiting...")
        break

    else:
        print("Unknown option.")
