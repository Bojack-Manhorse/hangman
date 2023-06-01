import random

word_list = ["Mango", "Melon", "Watermelon", "Strawberries", "Grapes"]

word = random.choice(word_list)

print(word)

def check_guess(guess, word):
    guess_in_lower_case = guess.lower()
    if guess_in_lower_case in word.lower():
        print(f"Good guess! {guess_in_lower_case} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False
        

def ask_for_input():
    while True:
        guess = input("Guess a letter!")
        if len(guess) == 1 and guess.isalpha():
            print("That's a valid input!")
            if check_guess(guess, word): #check_guess returns a truth value
                break
        else:
            print("That's not a valid input!")

ask_for_input()