first = int(input("Insert first integer: "))
second = int(input("Insert second integer: "))

# Compare the integers
if first > second:
	print("First integer is greater.")
elif second > first:
	print("Second integer is greater.")
else:
	print("Integers are the same.")

# Calculate the sum
sum_numbers = first + second
print("Sum:", sum_numbers)

# Check if the sum is even or odd
if sum_numbers % 2 == 0:
	print("Sum is even.")
else:
	print("Sum is odd.")