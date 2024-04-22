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

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess!")
            if attempts == 0:
                print("Sorry, you're out of attempts! The word was:", word_to_guess)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations, you've guessed the word:", word_to_guess)
            break

if _name_ == "_main_":
    hangman()
