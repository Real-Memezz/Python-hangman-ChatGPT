import random

WORDS = ["python", "java", "ruby", "javascript", "html", "css"]
MAX_TRIES = 7

def choose_word(words):
    return random.choice(words)

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        else:
            return guess

def display_word(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def display_hangman(tries):
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """
    ]
    print(stages[tries])

def play_game():
    print("Welcome to Hangman!")
    word = choose_word(WORDS)
    guesses = set()
    wrong_guesses = 0

    while True:
        display_hangman(wrong_guesses)
        display_word(word, guesses)

        if wrong_guesses == MAX_TRIES:
            print("Sorry, you ran out of guesses. The word was:", word)
            break

        if set(word) == guesses:
            print("Congratulations, you guessed the word!")
            break

        guess = get_guess()
        if guess in guesses:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guesses.add(guess)
        else:
            print("Sorry, that letter is not in the word.")
            wrong_guesses += 1

    play_again = input("Would you like to play again? (y/n)").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

play_game()
