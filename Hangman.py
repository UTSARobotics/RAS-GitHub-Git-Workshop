import random


# Function to choose a random word from the word bank
def choose_word():
    words = ["python", "hangman", "github", "repository", "commit", "branch", "merge", "pull", "push",
             "developer", "algorithm", "function", "variable", "iteration", "recursion", "syntax", "debugging",
             "framework", "compilation", "execution", "inheritance", "encapsulation", "polymorphism", "abstraction",
             "database", "interface", "protocol", "parameter", "exception", "argument", "namespace", "constructor",
             "compiler", "interpreter", "loop", "condition", "array", "pointer", "reference", "object", "class",
             "method", "attribute", "module", "package", "statement", "expression", "operator", "operand", "constant",
             "literal", "keyword", "debugger", "binary", "hexadecimal", "octal", "float", "integer", "string",
             "boolean"]
    return random.choice(words)


# Function to display the word with guessed letters revealed
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Function to display the available letters that have not been guessed yet
def display_available_letters(guessed_letters):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    available_letters = sorted(alphabet - guessed_letters)
    return " ".join(available_letters)


# Main function to run the Hangman game
def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))  # Show current state of the word
        print("Available letters:", display_available_letters(guessed_letters))  # Show remaining letters
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
        else:
            print("Correct!")

        # Check if the player has guessed all letters in the word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    # If player runs out of attempts, reveal the word
    print("\nGame over! The word was:", word)


# Run the game if the script is executed directly
if __name__ == "__main__":
    hangman()
