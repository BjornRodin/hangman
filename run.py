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
total_score = 0


def intro():
    """
    Gameintro showing rules to the user.
    asking for the username the user want to use,
    we check so it is a valid input.
    """
    print("Welcome to a game of Hangman!\n")
    print(graphic_start())
    print("The rules are simple:")
    print("1. You are presented with a number of underscores,")
    print("   that is the length of the word.")
    print("2. Guess 1 letter at a time by entering the letter,")
    print("   and then click 'Enter'.")
    print("3. If the letter is correct,")
    print("   it replaces the corresponding underscore(s).")
    print("4. If the letter is incorrect, you lose 1 of your guesses.")
    print("   4a. The number of guesses depends on the length of the word.")
    print("   4b. Loose all guesses and you have lost the game.")
    print("5. If you guessed all letters in the word, you win!")
    print("6. Shorter words score better than longer ones")
    print("   and more remaining guesses also improve the score.\n")
    print("Let's play!")

    username = ""
    while True:
        username = input("\nEnter your Username: \n")
        if not username.isalnum():
            print("Your Username has to be letters or numbers only.")
            continue
        elif len(username) < 3:
            print("Your Username has to be at least 3 characters long.")
            continue
        elif username_exists(username):
            print("That username already exists. Please enter another.")
            continue
        else:
            print(f"\nHello {username}, when you are ready to play,")
        return username


def username_exists(username):
    """
    Used to access previous usernames in spreadsheet,
    checking if users preferred username already exist.
    """
    scores = SHEET.worksheet('scores')
    usernames = scores.col_values(1)
    return username in usernames


def random_word():
    """
    Making the game find a word randomly from the 'words' variable I previously
    got from the spreadsheet.
    Because the word is still in a list,
    we have to remove [] and '' with the strip function
    """
    non_empty_cells = [word for word in words if word[0].strip()]
    word_list = random.choice(non_empty_cells)
    return word_list[0].strip()


def graphic_start():
    """
    Graphics for intro to make the user recognize the game quicker.
    """
    return ("   |-----|  \n"
            "   |     |  \n"
            "   |        \n"
            "   |        \n"
            "   |        \n"
            "  /|\\      \n"
            " / | \\     \n")


def graphic(guesses_remaining):
    """
    Graphics used throughout the game depending guesses_remaining.
    """
    if guesses_remaining > 9:
        return ("            \n"
                "            \n"
                "            \n"
                "            \n"
                "   |        \n"
                "   |        \n"
                "   |        \n")
    elif guesses_remaining > 8:
        return ("            \n"
                "            \n"
                "            \n"
                "            \n"
                "   |        \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 7:
        return ("   |        \n"
                "   |        \n"
                "   |        \n"
                "   |        \n"
                "   |        \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 6:
        return ("   |-----   \n"
                "   |        \n"
                "   |        \n"
                "   |        \n"
                "   |        \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 5:
        return ("   |-----|  \n"
                "   |     |  \n"
                "   |        \n"
                "   |        \n"
                "   |        \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 4:
        return ("   |-----|  \n"
                "   |     |  \n"
                "   |     0  \n"
                "   |        \n"
                "   |        \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 3:
        return ("   |-----|  \n"
                "   |     |  \n"
                "   |     0  \n"
                "   |     |  \n"
                "   |     |  \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 2:
        return ("   |-----|  \n"
                "   |     |  \n"
                "   |     0  \n"
                "   |   \\|  \n"
                "   |     |  \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 1:
        return ("   |-----|  \n"
                "   |     |  \n"
                "   |     0  \n"
                "   |   \\|/ \n"
                "   |     |  \n"
                "  /|\\      \n"
                " / | \\     \n")
    elif guesses_remaining > 0:
        return ("   |-----|  \n"
                "   |     |  \n"
                "   |     0  \n"
                "   |   \\|/ \n"
                "   |     |  \n"
                "  /|\\  /   \n"
                " / | \\     \n")
    else:
        return ("   |-----|  \n"
                "   |     |  \n"
                "   |     0  \n"
                "   |   \\|/ \n"
                "   |     |  \n"
                "  /|\\  / \\\n"
                " / | \\     \n")


def initialize():
    """
    Setting up game variables and returning as a tuple to be used later.
    """
    word = random_word().upper()
    word_length = len(word)
    word_hidden = ['_' for _ in range(word_length)]
    guesses_remaining = calculate_guesses(word_length)
    letters_guessed = []
    game_over = False
    print(word)
    return (word,
            word_length,
            word_hidden,
            guesses_remaining,
            letters_guessed,
            game_over)


def calculate_guesses(word_length):
    if word_length <= 3:
        guesses_remaining = 10
    elif word_length <= 6:
        guesses_remaining = 8
    elif word_length <= 9:
        guesses_remaining = 6
    else:
        guesses_remaining = 4
    return guesses_remaining


def get_user_input(letters_guessed, guesses_remaining, word_hidden):
    """
    Print graphics corresponding to how many guesses is left.
    Print the current state of the hidden word.
    Print all previously guessed letters.
    Print remaining guesses.
    Asking user for their input/guess. It then checks so it is valid.
    """
    print(graphic(guesses_remaining))
    print(' '.join(word_hidden))
    print(f"Letters guessed: {', '.join(letters_guessed)}")
    print(f"You have {guesses_remaining} guesses remaining.")
    guess = input("Guess a letter: \n").upper()
    if guess.isalpha() and len(guess) == 1:
        return guess
    else:
        error_message = (
            "ValueError: Your guess is either not in the alphabet,"
            "or is not 1 character long.\n"
            f"Your guess was '{guess.upper()}', try again.\n"
        )
        raise ValueError(error_message)


def update_hidden_word(word, word_hidden, guess, word_length):
    """
    When correct letter is chosen it replaces the '_' within the hidden word.
    """
    print(f"\nGood choice! The letter '{guess.upper()}' is in the word.\n")
    for i in range(word_length):
        if word[i] == guess:
            word_hidden[i] = guess


def guess_not_word(guesses_remaining, guess, word):
    """
    Check if there is any guesses remaining, if not, game is over.
    Else user is presented with the guess saying it's wrong.
    """
    if guesses_remaining == 0:
        print(graphic(guesses_remaining))
        print(f"GAME OVER!\nThe word was '{word}'.")
        print(f"\nYour current total score is: {total_score}")
        return True
    else:
        print(f"\nWrong! The letter '{guess.upper()}' is not in the word!\n")


def game_won(word_hidden, word, word_length):
    """
    Check if the hidden word is equal to word.
    Ending game if it is.
    """
    if ''.join(word_hidden) == word:
        win_message = (
            "CONGRATULATIONS!\n"
            f"You have guessed the word '{word}' and win the game!"
        )
        print(win_message)
        return True
    else:
        return False


def add_score(word_length, guesses_remaining):
    global total_score
    base_score = 100
    word_score = base_score - (word_length * 5)
    guess_score = guesses_remaining * 5
    total_score += word_score + guess_score


def gameinfo_to_sheet(username, total_score):
    """
    Updating spreadsheet with the username the user chose and their final score
    if their score is atleast in the top 5 of all previous scores.
    Then printing top 5 to a scoreboard.
    """
    print("Updating scoreboard...\n")
    worksheet = SHEET.worksheet('scores')
    # Written with help from
    # https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
    scores = worksheet.get_all_values()[1:]
    scores.sort(key=lambda row: int(row[1]), reverse=False)
    if len(scores) < 5 or total_score > int(scores[-5][1]):
        worksheet.append_row([username, total_score])
        top5_update_message = (
            "Congratulations!\nYou are in the top 5!"
            f"Successfully updated your username '{username}'\n"
            f"and your total score '{total_score}' to scoreboard!\n"
        )
        print(top5_update_message)
        scores.append([username, total_score])
        scores.sort(key=lambda row: int(row[1]), reverse=False)
        scores = scores[-5:]
    else:
        print(f"Sorry {username}, your score is not in the top 5.")
        scores = scores[-5:]

    print("\nTop 5 scores in Scoreboard:")
    for i, row in enumerate(scores[::-1]):
        print(f"{i+1}. {row[0]} - {row[1]}pts")
        print()


def playgame():
    """
    Getting the variables from initialize function.
    Printing the length of the word to the user.
    While loop going through the game as long as
    there is guesses remaining and game not over.
    Assigning value 'guess' for every input the user provides.
    Value 'guess' is then compared to variables 'letters_guessed' and 'word'
    game continue by calling previous functions depending on which stage it is.
    """
    global total_score
    word, word_length, word_hidden, \
        guesses_remaining, letters_guessed, game_over = initialize()
    print(f"\nThe word has {word_length} letters in it. Good luck!\n")

    # Looping through the game, calling functions when needed.
    while guesses_remaining > 0 and not game_over:
        try:
            guess = get_user_input(
                letters_guessed,
                guesses_remaining,
                word_hidden
            )
            if guess in letters_guessed:
                letters_guessed_message = (
                    f"\nThe letter '{guess.upper()}' has already been guessed."
                    "\nTry another letter!\n""
                )
                print(letters_guessed_message)
            elif guess in word:
                letters_guessed.append(guess)
                update_hidden_word(word, word_hidden, guess, word_length)
                game_over = game_won(word_hidden, word, word_length)
                if game_over:
                    add_score(word_length, guesses_remaining)
                    print(f"\nYour current total score is: {total_score}")
                    break
            elif guess not in word:
                guesses_remaining -= 1
                letters_guessed.append(guess)
                guess_not_word(guesses_remaining, guess, word)
        except ValueError as ve:
            print(ve)


def main_functions():
    """
    Running all main functions for the game.
    Make the user able to keep playing if they want to.
    """
    global total_score
    username = intro()
    play_again = True
    while play_again:
        input("press Enter to start the game...")
        playgame()
        play_again = input("\nWould you like to play again? (y/n)\n").lower()
        play_again = play_again == "y"
        if not play_again:
            thanks_message = (
                "\nThanks for playing!\n"
                f"Your final score was: {total_score}\n"
            )
            print(thanks_message)
            gameinfo_to_sheet(username, total_score)
            total_score = 0


if __name__ == '__main__':
    main_functions()
