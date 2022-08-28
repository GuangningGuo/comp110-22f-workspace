"""Ex01 - Chardle - A cute step towards Wordle."""
__author__ = "730558895"

word: str = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
    
character: str = input("Enter a single character:")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for", character, "in", word)

count: int = 0 #count the number of matching characters
if character == word[0]:
    count = count + 1
    print(character + " found at index 0")

if character == word[1]:
    count = count + 1
    print(character + " found at index 1")

if character == word[2]:
    count = count + 1
    print(character + " found at index 2")

if character == word[3]:
    count = count + 1
    print(character + " found at index 3")

if character == word[4]:
    count = count + 1
    print(character + " found at index 4")

print(count, "instances of", character, "found in", word)

