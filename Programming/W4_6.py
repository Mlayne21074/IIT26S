print("Program starting.")

Value = int(input("Insert a positive integer: "))
Sequence = str(Value)
Steps = 0

while Value != 1:
    if Value % 2 == 0:
        Value = Value // 2
    else:
        Value = Value * 3 + 1

    Sequence = Sequence + " -> " + str(Value)
    Steps = Steps + 1

print(Sequence)
print(f"Sequence had {Steps} total steps.")

print("Program ending.")
