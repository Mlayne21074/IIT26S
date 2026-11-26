print("Program starting.")

Word = input("Insert a closed compound word: ")

print(f"The word you inserted is '{Word}' and in reverse it is '{Word[::-1]}'.")
print(f"The inserted word length is {len(Word)}")
print(f"First character is '{Word[0]}'")

print()
print("Take substring from the inserted word by inserting...")
Start = int(input("1) Starting point: "))
End = int(input("2) Ending point: "))
Step = int(input("3) Step size: "))

Substring = Word[Start:End:Step]

print()
print(f"The word '{Word}' sliced to the defined substring is '{Substring}'.")
print("Program ending.")
