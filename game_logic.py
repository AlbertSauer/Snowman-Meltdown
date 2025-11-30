import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

MAX_MISTAKES = len(STAGES) - 1  # last stage index

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and the current progress on the word."""
    print("\n" + "=" * 40)
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:         ", display_word)
    if guessed_letters:
        print("Guessed:      ", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed:       (none yet)")
    print("=" * 40 + "\n")

def is_word_fully_guessed(secret_word, guessed_letters):
    """Checks if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def get_valid_guess(guessed_letters):
    """Prompt the user until they enter a valid, new single letter."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        # Input validation: single alphabetical character only
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a SINGLE alphabetical letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print("⚠️  You already guessed that letter. Try a different one.\n")
            continue

        return guess

def play_single_game():
    """Plays one round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!")
    # For debugging/testing, you can uncomment this:
    # print(f"(Debug) Secret word is: {secret_word}")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win
        if is_word_fully_guessed(secret_word, guessed_letters):
            print("🎉 You saved the snowman!")
            print(f"The word was: {secret_word}\n")
            break

        # Check loss
        if mistakes >= MAX_MISTAKES:
            # Show final stage again just in case
            print(STAGES[mistakes])
            print("💥 Oh no! The snowman melted completely.")
            print(f"The word was: {secret_word}\n")
            break

        # Get a valid guess from user
        guess = get_valid_guess(guessed_letters)

        # Record guess
        guessed_letters.append(guess)

        # Check correctness
        if guess in secret_word:
            print(f"✅ Nice! '{guess}' is in the word.\n")
        else:
            mistakes += 1
            print(f"❌ Sorry, '{guess}' is not in the word.\n")

def ask_play_again():
    """Ask the user if they want to play again; returns True/False."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")

def play_game():
    """Main entry point: handles replay loop."""
    while True:
        play_single_game()
        if not ask_play_again():
            print("\nThanks for playing Snowman Meltdown! Goodbye! ❄️")
            break

if __name__ == "__main__":
    play_game()
