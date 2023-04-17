"""
Imported dependencies such as gspread to be able to access the spreadsheet
Import random to be able to use the mathematical function of random
"""
import random
import string
import gspread
from google.oauth2.service_account import Credentials

"""
Assigning credentials from the API's to access the spreadsheet and it's content
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

wordlist = SHEET.worksheet('words')
words = wordlist.get_all_values()

def intro():
    """
    Gameintro showing the user the rules
    asking for the username the user want to use
    asking the user if they want to play by entering "Y" or "N" and then click enter
    """
    print("Welcome to a game of Hangman!")
    print()
    print(graphic_start())
    print("The rules are simple:")
    print("1. You are presented with a number of underscores, that is the length of the word.")
    print("2. Guess 1 letter at a time by entering the letter and then click 'Enter'.")
    print("3. If the letter is correct, it replaces the corresponding underscore(s).")
    print("4. If the letter is incorrect, you lose 1 of your 6 guesses. \nLoose all 6 guesses and you have lost the game.")
    print("5. If you guessed all letters in the word, you win!")
    print()
    print("Let's play!")

    username = ""
    while True:
        username = input("Enter your Username: \n")
        
        if not username.isalpha():
            print("Your Username has to be letters only.")
            continue
        else:
            print(f"Hello {username}, when you are ready to play,")
        return username    

def random_word():
    """
    Making the game find a word randomly from the 'words' variable I previously
    got from the spreadsheet.
    Because the word is still in a list we have to remove [] and '' with the strip function
    """
    non_empty_cells = [word for word in words if word[0].strip()]
    word_list = random.choice(non_empty_cells)
    return word_list[0].strip()

def graphic_start():
    return("   |-----|  \n"
           "   |     |  \n"
           "   |        \n"
           "   |        \n"
           "  /|\\      \n"
           " / | \\     \n")

def playgame():
    """
    Getting the random word then replacing it with underscores.
    Graphic of the gallows.
    Starting variables specified for start of each game, to store guessed letters
    for example
    """
    word = random_word().upper()
    word_length = len(word)
    print(word)
    word_hidden = (' '.join(['_' for letter in word]))
    print(word_hidden)

    guesses_remaining = 6
    letters_guessed = []
    game_over = False
    # Looping through the game, checking if letter etc
    while game_over is False and guesses_remaining > 0:
        print(f"The word has {word_length} letters in it. Good luck!")
        print(f"You have {guesses_remaining} guesses remaining.")
        print()
        guess = input("Guess a letter: \n").upper()
        
        if guess.isalpha() and len(guess) == 1:
            if guess in letters_guessed:
                print(f"The letter '{guess.upper()}' has already been guessed.")
                print("Try another letter!\n")
            elif guess not in word:
                print(f"Wrong! The letter '{guess.upper()}' is not in the word.")
                print("Try again!\n")
                letters_guessed.append(guess)
                guesses_remaining -= 1
            elif guess in word:
                print(f"Good choice! The letter '{guess.upper()}' is in the word.\n")
                letters_guessed.append(guess)
            else:
                print("Error: Something went wrong, try again.\n")
        else:
            print(f"Error: Your guess is either not in the alphabet, or is not 1 character long.\n"
            f"Your guess was '{guess.upper()}', try again.\n")
    else:
        print("ValueError: Please try again, make sure it is a letter.")

def main_functions():
    """
    Running all main functions for the game
    """
    username = intro()
    input("press Enter to start the game...")
    playgame()
main_functions()