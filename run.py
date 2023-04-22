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
           "   |        \n"
           "  /|\\      \n"
           " / | \\     \n")

def graphic(guesses_remaining):
    if guesses_remaining > 5:
        return("   |-----|  \n"
               "   |     |  \n"
               "   |        \n"
               "   |        \n"
               "   |        \n"
               "  /|\\      \n"
               " / | \\     \n")
    elif guesses_remaining > 4:
        return("   |-----|  \n"
               "   |     |  \n"
               "   |     0  \n"
               "   |        \n"
               "   |        \n"
               "  /|\\      \n"
               " / | \\     \n")
    elif guesses_remaining > 3:
        return("   |-----|  \n"
               "   |     |  \n"
               "   |     0  \n"
               "   |     |  \n"
               "   |     |  \n"
               "  /|\\      \n"
               " / | \\     \n")
    elif guesses_remaining > 2:
        return("   |-----|  \n"
               "   |     |  \n"
               "   |     0  \n"
               "   |    \|  \n"
               "   |     |  \n"
               "  /|\\      \n"
               " / | \\     \n")
    elif guesses_remaining > 1:
        return("   |-----|  \n"
               "   |     |  \n"
               "   |     0  \n"
               "   |    \|/ \n"
               "   |     |  \n"
               "  /|\\      \n"
               " / | \\     \n")
    elif guesses_remaining > 0:
        return("   |-----|  \n"
               "   |     |  \n"
               "   |     0  \n"
               "   |    \|/ \n"
               "   |     |  \n"
               "  /|\\  /   \n"
               " / | \\     \n")
    else:
        return("   |-----|  \n"
               "   |     |  \n"
               "   |     0  \n"
               "   |    \|/ \n"
               "   |     |  \n"
               "  /|\\  / \ \n"
               " / | \\     \n")

def initialize():
    """
    Setting up game variables and returning as a tuple to be used later.
    """
    word = random_word().upper()
    word_length = len(word)
    word_hidden = ['_' for _ in range(word_length)]
    guesses_remaining = 6
    letters_guessed = []
    game_over = False
    print(word)
    return word, word_length, word_hidden, guesses_remaining, letters_guessed, game_over

def get_user_input(letters_guessed, guesses_remaining):
    print(graphic(guesses_remaining))
    print(f"Letters guessed: {', '.join(letters_guessed)}")
    guess = input("Guess a letter: \n").upper()
    if guess.isalpha() and len(guess) == 1:
        return guess
    else:
        raise ValueError(f"ValueError: Your guess is either not in the alphabet, or is not 1 character long.\n"
            f"Your guess was '{guess.upper()}', try again.\n")

def update_hidden_word(word, word_hidden, guess, word_length):
    print(f"\nGood choice! The letter '{guess.upper()}' is in the word.\n")
    for i in range(word_length):
        if word[i] == guess:
            word_hidden[i] = guess
    print(' '.join(word_hidden))

def guess_not_word(guesses_remaining, guess, word):
    if guesses_remaining == 0:
        print(f"GAME OVER! The word was '{word}'.")
        return True
    else:
        print(f"Wrong! The letter '{guess.upper()}' is not in the word, guess again!\n")

def game_won(word_hidden, word):
    if ''.join(word_hidden) == word:
        print(f"CONGRATULATIONS! You have guessed the word '{word}' and win the game!")
        return True
    else:
        return False

def playgame():
    """
    Getting the random word then replacing it with underscores.
    Graphic of the gallows.
    Starting variables specified for start of each game, to store guessed letters
    for example
    """
    word, word_length, word_hidden, guesses_remaining, letters_guessed, game_over = initialize()
    print(f"The word has {word_length} letters in it. Good luck!\n")

    # Looping through the game, calling functions when needed.
    while guesses_remaining > 0 and not game_over:
        print(f"You have {guesses_remaining} guesses remaining.")
        print()
        try:
            #print(letters_guessed)
            guess = get_user_input(letters_guessed, guesses_remaining)
            if guess in letters_guessed:
                print(f"The letter '{guess.upper()}' has already been guessed.")
                print("Try another letter!\n")
            elif guess in word:
                letters_guessed.append(guess)
                update_hidden_word(word, word_hidden, guess, word_length)
                game_over = game_won(word_hidden, word)
                if game_over:
                    break
            elif guess not in word:
                guesses_remaining -= 1
                letters_guessed.append(guess)
                guess_not_word(guesses_remaining, guess, word)
            """
            else:
                letters_guessed.append(guess)
                if guess in word:
                    update_hidden_word(word, word_hidden, guess, word_length)
                    game_over = game_won(word_hidden, word)
                    if game_over:
                        break
                elif guess not in word:
                    guesses_remaining -= 1
                    if guesses_remaining == 0:
                        print(f"GAME OVER! The word was '{word}'.")
                        break
                    else:
                        print("Try again!\n")
                else:
                    if word_hidden == word:
                        print(f"CONGRATULATIONS! You have guessed the word '{word}' and win the game!")
                        game_over = True
                        """
        except ValueError as ve:
            print(ve)

def main_functions():
    """
    Running all main functions for the game
    """
    username = intro()
    input("press Enter to start the game...")
    playgame()
main_functions()