# MJ Patten
# CIS256 Fall 2025
# EX 4

import random

# Create a predefined list of words
word_list = ["orange", "yellow", "purple"]

def choose_word(words):
    """Return a random word from the given list."""
    return random.choice(words)

def reveal_letters(word, hidden, letter):
    """Reveal letter positions in the hidden word."""
    hidden_list = list(hidden)
    for i, char in enumerate(word):
        if char == letter:
            hidden_list[i] = letter
    return "".join(hidden_list)

def is_correct_guess(word, guess):
    """Return True if the full-word guess matches the word."""
    return guess == word


def play_game():
    random_word = choose_word(word_list)
    hidden = "*" * len(random_word)
    attempts = 6

    print("Guess the Color!!")
    print(hidden)

    while True:
        guess = input("\nEnter a letter OR guess the entire word: ").lower()

    # User guesses the entire word
        if len(guess) > 1:
            if is_correct_guess(random_word, guess):
                print(f"Correct! The word was {random_word}! You win!")
                break
            else:
                print("Wrong guess!")
                continue

    # User guesses a single letter
        if guess in random_word:
            print(f"The letter '{guess}' IS in the word!")
            hidden = reveal_letters(random_word, hidden, guess)
        else:
            attempts -=1
            print(f"The letter '{guess}' IS NOT in the word.")
            print(f"Attempts left: {attempts}")

        print("Current word:", hidden)

        if "*" not in hidden:
            print(f"\nCongrats! You guessed the word: {random_word}")
            break

    # Out of attempts
        if attempts == 0:
            print(f"\nYou ran out of attempts! The word was: {random_word}")
            break

if __name__ == "__main__":
    play_game()