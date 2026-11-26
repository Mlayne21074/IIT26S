print("Temperature conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")

Choice = input("Choose an option: ")

if Choice == "1":
    Celsius = float(input("Enter temperature in Celsius: "))
    Fahrenheit = Celsius * 1.8 + 32
    print(f"{round(Fahrenheit, 1)} °F")

elif Choice == "2":
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = (Fahrenheit - 32) / 1.8
    print(f"{round(Celsius, 1)} °C")

elif Choice == "3":
    print("Goodbye!")

else:
    print("Invalid choice.")
