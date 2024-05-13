# hangman.py
import random

class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 6
        self.guessed_letters = set()

    def display_word(self):
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def guess(self, letter):
        if letter not in self.word:
            self.remaining_guesses -= 1
        self.guessed_letters.add(letter)

    def is_game_over(self):
        return self.remaining_guesses == 0 or set(self.word).issubset(self.guessed_letters)

def play_game():
    from words import word_list

    word_to_guess = random.choice(word_list)
    game = Hangman(word_to_guess)

    print("Welcome to Hangman!")
    print("Guess the word: ", game.display_word())

    while not game.is_game_over():
        guess = input("Enter your guess: ").lower()
        game.guess(guess)
        print("Word:", game.display_word())
        print("Remaining guesses:", game.remaining_guesses)

    if game.remaining_guesses == 0:
        print("You lose! The word was", word_to_guess)
    else:
        print("Congratulations! You guessed the word", word_to_guess, "correctly!")

if __name__ == "__main__":
    play_game()

