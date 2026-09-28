word_first = input("Insert a word: ")
character = input("Insert a character: ")

# Check if the character exists in the first word
if character in word_first:
	print(f'Word "{word_first}" contains character "{character}"')
else:
	print(f'Word "{word_first}" doesn\'t contain character "{character}"')

# Ask for the second word
word_second = input("Insert one more word: ")

# Compare the words alphabetically
if word_first < word_second:
	print(f'The first word "{word_first}" is before the second word "{word_second}" alphabetically.')
elif word_second < word_first:
	print(f'The second word "{word_second}" is before the first word "{word_first}" alphabetically.')
else:
	print(f'Both inserted words are the same alphabetically, "{word_first}"')