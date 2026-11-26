print("Program starting.")
print()
print("Check multiplicative persistence.")

Value = input("Insert an integer: ")
Steps = 0

while len(Value) > 1:
    Product = 1
    Calculation = ""

    for Digit in Value:
        Product = Product * int(Digit)

        if Calculation == "":
            Calculation = Digit
        else:
            Calculation = Calculation + " * " + Digit

    print(Calculation + " = " + str(Product))

    Value = str(Product)
    Steps = Steps + 1

print("No more steps.")
print()
print(f"This program took {Steps} step(s).")
print()
print("Program ending.")
