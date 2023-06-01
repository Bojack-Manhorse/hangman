import random

word_list = ["Mango", "Melon", "Watermelon", "Strawberries", "Grapes"]

word = random.choice(word_list)

print(word)

guess = ""

while True:
    guess = input("Guess a letter!")

    if len(guess) == 1 and guess.isalpha():
        print("That's a valid input!")
        if guess in list(word.upper()) or guess in list(word.lower()):
            print("Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("That's not a valid input!")



