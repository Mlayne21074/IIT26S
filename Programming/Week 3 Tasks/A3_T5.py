print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")

choice = input("Choose an option: ")

if choice == "1":
	celsius = float(input("Enter temperature in °C: "))
	fahrenheit = celsius * 1.8 + 32
	print(f"{fahrenheit:.1f} °F")
elif choice == "2":
	fahrenheit = float(input("Enter temperature in °F: "))
	celsius = (fahrenheit - 32) / 1.8
	print(f"{celsius:.1f} °C")
elif choice == "3":
	print("Exiting...")
else:
	print("Unknown option.")