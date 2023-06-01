import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = [" " for x in range(5)]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess_lower_case = guess.lower()
        if guess_lower_case in self.word.lower():
            print(f"Good guess! {guess_lower_case} is in the word.")
            for letter_in_word in list(self.word):
                if guess_lower_case == letter_in_word:
                    self.list_of_guesses[self.word_guessed.index(" ")] = letter_in_word
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess_lower_case} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter!")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that character!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

my_game = Hangman(["Mango", "Melon", "Watermelon", "Strawberries", "Grapes"])

print(len(set("AAbb")))

my_game.ask_for_input()
