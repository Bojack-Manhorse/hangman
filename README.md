# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Currently the "milestone_2.py" file contains a list of 5 strings representing fruits. It then picks one at random using the random module. Then it asks the user for some input, and finally checks if the input is a string containing one character and is contained in the alphabet.

The file "milestone_3.py" randomly selects a fruit, asks the user for some input, then checks if the input is a valid letter then checks if the letter is in the fruit. This is done via two functions, check_guess() which checks if a given letter in a giver word, and ask_for_input(), which creates a loop that keeps sking the user for a valid input.

In "milestone_4.py" we turn everything into a class.

In "milestone_5,py" we define the play_game() function which creates a loop which tracks the porgress and number of lives left when playing. It ends the game when the player wins or loses. Also added a break in the ask_for_input function after the check_input() function was callled.