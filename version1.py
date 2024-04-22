import random

def choose_word():
    words = ["hangman", "python", "computer", "program", "language", "game", "code"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def draw_hangman(attempts):
    stages = [
        """
           _______
          |/      |
          |     
          |     
          |     
          |   
         |""",
        """
           _______
          |/      |
          |      (_)
          |     
          |     
          |   
         |""",
        """
           _______
          |/      |
          |      (_)
          |       |
          |       |
          |   
         |""",
        """
           _______
          |/      |
          |      (_)
          |      /|
          |       |
          |   
         |""",
        """
           _______
          |/      |
          |      (_)
          |      /|\\
          |       |
          |   
         |""",
        """
           _______
          |/      |
          |      (_)
          |      /|\\
          |       |
          |      /
         |""",
        """
           _______
          |/      |
          |      (_)
          |      /|\\
          |       |
          |      / \\
         |"""
    ]
    return stages[attempts]

def word_relationship(word):
    relationships = {
        'python': 'a programming language',
        'hangman': 'a guessing game',
        'game': 'a form of entertainment',
        'programming': 'the act of writing code',
        'computer': 'a machine that performs computations',
        'science': 'the study of the natural world'
    }
    return relationships.get(word, 'something interesting')

def hangman():
    while True:
        word_to_guess = choose_word()
        guessed_letters = []
        attempts = 6
        clue_given = False

        print("Welcome to Hangman!")
        print("Try to guess the word.")
        print("You have 6 attempts to guess the word correctly.")
        print("Here's a clue about the word: " + word_relationship(word_to_guess))

        while attempts > 0:
            print(draw_hangman(6 - attempts))
            print(display_word(word_to_guess, guessed_letters))
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in word_to_guess:
                attempts -= 1
                print(f"Incorrect guess! You have {attempts} attempts left.")
                if attempts == 0:
                    print("Sorry, you lost. The word was:", word_to_guess)
                    break
            else:
                print("Correct guess!")

            if all(letter in guessed_letters for letter in word_to_guess):
                print("Congratulations, you won!")
                break
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if _name_ == "_main_":
    hangman()
