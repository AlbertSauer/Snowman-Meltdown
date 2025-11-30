import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

MAX_MISTAKES = len(STAGES) - 1  # last stage is fully melted


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and the current progress on the word."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")
    print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
    print("\n")


def is_word_fully_guessed(secret_word, guessed_letters):
    """Checks if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # For debugging / testing only; remove later:
    print("(Debug) Secret word is:", secret_word)
    print()

    # Main game loop
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check for end conditions before asking for a new guess
        if is_word_fully_guessed(secret_word, guessed_letters):
            print("You saved the snowman!")
            print(f"The word was: {secret_word}")
            break

        if mistakes >= MAX_MISTAKES:
            print(STAGES[mistakes])  # show final melted state
            print("Oh no! The snowman melted completely.")
            print(f"The word was: {secret_word}")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        # Add guess to guessed letters
        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Nice! '{guess}' is in the word.\n")
        else:
            mistakes += 1
            print(f"Oops! '{guess}' is not in the word.\n")


if __name__ == "__main__":
    play_game()
