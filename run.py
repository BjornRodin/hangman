"""
Imported dependencies such as gspread to be able to access the spreadsheet
"""
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
            print(f"Hello {username}, when you are ready to play, Press Enter.")
        return username    


def playgame():
    """
    Running all main functions for the game
    """
    username = intro()
playgame()