import random

# List of words for the game
words = ["python", "java", "ruby", "javascript", "html", "css"]

# Function to choose a random word from the list
def choose_word(words):
    return random.choice(words)

# Function to print the current state of the hangman
def print_hangman(tries):
    stages = [  # Final stage: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Stage 6: head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # Stage 5: head, torso, both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # Stage 4: head, torso, one arm, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     / \\
                   -
                """,
                # Stage 3: head, torso, one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # Stage 2: head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # Stage 1: head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # Initial stage: empty gallows
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    print(stages[tries])

# Function to check if the player has won
def check_win(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    return True

# Main function to run the game
def play_game():
    print("Welcome to Hangman!")
    word = choose_word(words)
    word_letters = set(word)
    used_letters = set()
    tries = 7

    while tries > 0:
        print_hangman(tries)
        print("Used letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_list))

        guess = input("Guess a letter: ").lower()
        if guess in used_letters:
            print("You already guessed that letter!")
        elif guess in word_letters:
            print("Good guess!")
            used_letters.add(guess)
            if check_win(word, used_letters):
                print_hangman(0)
                print("Congratulations! You win!")
                break
        else:
            print("Sorry, that letter is not in the word.")
            used_letters.add(guess)
            tries -= 1

    if tries == 0:
        print_hangman(0)
        print("Sorry, you ran out of tries. The word was", word)

# Call the main function to start the game
play_game()
