print("Program starting.")

number = int(input("Insert a positive integer: "))

print(number, end="")

steps = 0

while number != 1:
	if number % 2 == 0:
		number = number // 2
	else:
		number = number * 3 + 1

	print("-->", number, end="")
	steps += 1

print()
print("Sequence had", steps, "total steps.")

print()
print("Program ending.")
