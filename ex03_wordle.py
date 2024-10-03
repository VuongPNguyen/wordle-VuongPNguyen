"""This is an actual wordle program."""

__author__ = "730670737"

# Funtion Section:


def contains_char(word: str, character: str) -> bool:
    """This function will see if the character is in a word."""
    assert len(character) == 1
    
    in_word: bool = False
    counter: int = 0

    while counter < len(word):
        if character == word[counter]:
            in_word = True
        counter += 1

    return in_word


def emojified(guess: str, secret_word: str) -> str:
    """Returns a string of emojies based on the strings."""
    assert len(guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    final_string = ""

    counter = 0
    yellow_letter = False
    
    while counter < len(secret_word):
        yellow_letter = contains_char(secret_word, guess[counter])

        if guess[counter] == secret_word[counter]:
            final_string += GREEN_BOX
        elif yellow_letter:
            final_string += YELLOW_BOX
        else:
            final_string += WHITE_BOX
        
        counter += 1
        yellow_letter = False
    
    return final_string


def input_guess(guess_length: int) -> str:
    """Ensures that the input has the correct amount of characters."""
    guess = input(f"Enter a {guess_length} character word: ")

    while len(guess) != guess_length:
        guess = input(f"That wasn't {guess_length} chars! Try again: ")
    
    return guess


def main() -> None:
    """The entry point of the programand main game loop."""
    secret: str = "codes"
    turn_counter: int = 0
    max_turns: int = 6
    user_guess: str = ""
    
    while (turn_counter < max_turns) and (user_guess != secret):
        turn_counter += 1
        print(f"=== Turn {turn_counter}/{max_turns} ===")

        user_guess = input_guess(len(secret))
        result = emojified(user_guess, secret)
        print(result)

    if user_guess == secret:
        print(f"You won in {turn_counter}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tommorow!")


if __name__ == "__main__":
    main()