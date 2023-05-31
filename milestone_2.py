import random

word_list = ["Mango", "Melon", "Watermelon", "Strawberries", "Grapes"]

word = random.choice(word_list)

#print(word)

guess = input("Guess a letter!")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("That's not a valid input!")