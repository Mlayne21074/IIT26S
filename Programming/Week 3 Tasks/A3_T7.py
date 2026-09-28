value = int(input("Insert an integer: "))

print("1. One multi-branched decision")
print("2. Independent if-statement decisions")
print("0. Exit")

choice = int(input("Your choice: "))

if choice == 1:
	if value >= 400:
		value = value + 44
	elif value >= 200:
		value = value + 22
	elif value >= 100:
		value = value + 11

	print("Result:", value)

elif choice == 2:
	if value >= 400:
		value = value + 44

	if value >= 200:
		value = value + 22

	if value >= 100:
		value = value + 11

	print("Result:", value)

elif choice == 0:
	print("Exiting...")

else:
	print("Unknown option.")