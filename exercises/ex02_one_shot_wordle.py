"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730558895"

secret_word: str = "python"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0

while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again:")

emoji: str = ""
check: bool = False


while i < len(secret_word):
    if guess_word[i] == secret_word[i]:
        emoji += GREEN_BOX
    else: 
        follow: int = 0
        check = False
        
        while follow < len(secret_word):
            if guess_word[i] == secret_word[follow]:
                check = True
            follow += 1
        if check is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i += 1
            
print(emoji)


if guess_word != secret_word:
    print("Not quite. Play again soon!")

if guess_word == secret_word:
    print("Woo! You got it!")
