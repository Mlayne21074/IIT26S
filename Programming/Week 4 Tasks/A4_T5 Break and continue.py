print("Program starting.")

starting_point = int(input("Insert starting point: "))
stopping_point = int(input("Insert stopping point: "))
inspection_point = int(input("Insert inspection point: "))

print()

valid = True

if starting_point >= stopping_point:
	print("Starting point value must be less than the stopping point value.")
	valid = False

if inspection_point < starting_point or inspection_point > stopping_point:
	print("Inspection value must be within the range of start and stop.")
	valid = False

if valid:
	print("First loop - inspection with break:")

	for number in range(starting_point, stopping_point):
		if number == inspection_point:
			break

		if number == inspection_point - 1:
			print(number)
		else:
			print(number, end=" ")

	print("Second loop - inspection with continue:")

	for number in range(starting_point, stopping_point):
		if number == inspection_point:
			continue

		if number == stopping_point - 1:
			print(number)
		else:
			print(number, end=" ")

	print()

print("Program ending.")
