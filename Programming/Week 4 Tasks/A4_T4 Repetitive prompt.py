print("Program starting.")

word_count = 0
character_count = 0

print()

word = input("Insert word (empty stops): ")

while word != "":
	word_count += 1
	character_count += len(word)
	word = input("Insert word (empty stops): ")

print()
print("You inserted:")
print("-", word_count, "words")
print("-", character_count, "characters")

print()
print("Program ending.")
