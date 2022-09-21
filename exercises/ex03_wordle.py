"""EX03 - Structured Wordle."""
__author__ = "730558895"


def contains_char(a: str, b: str) -> bool:
    """Check if character b is in word a."""
    i: int = 0
    assert len(b) == 1
    while i < len(a):
        if b == a[i]:
            return True
        else:
            i += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Turning words into emojis."""
    assert len(guess) == len(secret)
    emoji: str = ""
    it: int = 0
    while it < len(secret):
        if guess[it] == secret[it]:
            emoji += GREEN_BOX
            
        else:
            if contains_char(secret, guess[it]) is True:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        it += 1
    return emoji


def input_guess(len_guess: int) -> str:
    """Guiding the user to enter guess words of correct length."""
    guess = input(f"Enter a {len_guess} character word: ")
    while len(guess) != len_guess:
        guess = input(f"That wasn't {len_guess} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False
    while turn <= 6 and not win:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(5)
        secret: str = "codes"
        print(emojified(guess, secret))
        if guess != secret:
            turn += 1
        else:
            win = True
    if win is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()