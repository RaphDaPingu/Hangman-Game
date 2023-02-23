def print_welcome(MAX_TRIES):
    """Prints nice ASCII art, accompanied by an info message.
    :param MAX_TRIES: The number of tries left, which is always gonna be 6 at the start
    :type MAX_TRIES: int
    :return: none
    :rtype: none
    """
    
    print ("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")

    print("\nWelcome to Hangman!\nYou have " + str(MAX_TRIES) + " tries to guess the secret word!")

def choose_word(file_path, index):
    """Returns a word that is picked from file_path, in the index of the parameter index minus one.
    :param file_path: The file that contains a list of words
    :param index: The index of the word - works in a circular way
    :type file_path: file
    :type index: int
    :return wanted_word: The word that was associated with the parameter index
    :rtype: str
    """
    f = open(file_path, "r")
    sentence_data = f.read()

    sentence_list = []

    sentence_list = sentence_data.split(" ")
    
    for i in sentence_list:
        if (sentence_list.index(i) + 1 == index):
            wanted_word = i
        elif (index > len(sentence_list)):
            wanted_word = sentence_list[(index - 1) % ((len(sentence_list)))]
    
    return (wanted_word)

def print_hangman(num_of_tries):
    """Prints an ASCII art, according to the value of num_of_tries.
    :param num_of_tries: The number of tries the user has left to guess the secret word correctly
    :type num_of_tries: int
    :return: none
    :rtype: none
    """
    HANGMAN_PHOTOS = {
    "picture 1" :
    """
    x-------x
    """, 

    "picture 2" :
    """
    x-------x
    |
    |
    |
    |
    |
    """,

    "picture 3" :
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,

    "picture 4" :
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,

    "picture 5" :
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,

    "picture 6" :
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,

    "picture 7" :
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """}

    if (num_of_tries == 1):
        print(HANGMAN_PHOTOS["picture 1"])

    elif (num_of_tries == 2):
        print(HANGMAN_PHOTOS["picture 2"])

    elif (num_of_tries == 3):
        print(HANGMAN_PHOTOS["picture 3"])

    elif (num_of_tries == 4):
        print(HANGMAN_PHOTOS["picture 4"])

    elif (num_of_tries == 5):
        print(HANGMAN_PHOTOS["picture 5"])

    elif (num_of_tries == 6):
        print(HANGMAN_PHOTOS["picture 6"])

    elif (num_of_tries == 7):
        print(HANGMAN_PHOTOS["picture 7"])

def show_hidden_word(secret_word, old_letters_guessed):
    """Makes a string where it shows all correctly guessed letters inside secret_word, and all the other unguessed letters as "_".
    :param secret_word: The word the user is trying to guess
    :param old_letters_guessed: The letters the user has already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return guess_string: A string where there are all the correctly guessed letters inside secret_word, and all the other unguessed letters as "_"
    :rtype: str
    """
    guess_string = ""
    
    for i in secret_word:
        if (i in old_letters_guessed):
            guess_string += i
        else:
            guess_string += "_"

    guess_string = " ".join(guess_string) 
    
    return (guess_string)

def check_valid_input(letter_guessed, old_letters_guessed):
    """Determines if the user input is legal.
    :param letter_guessed: The user's guess
    :param old_letters_guessed: The letters that were already guessed
    :type letter_guessed: char / str
    :type old_letters_guessed: list
    :return: A flag that returns true if the input is a single English letter and was not already given as an input, false for all other cases
    :rtype: bool
    """
    
    flag = False

    lower_guessed = letter_guessed.lower()
    
    if ((len(lower_guessed) == 1) and (lower_guessed in "abcdefghijklmnopqrstuvwxyz") and (lower_guessed not in old_letters_guessed)):
        flag = True
    
    return (flag)

def letter_sorter(old_letters):
    """Shows the user the already guessed letters, sorted alphabetically
    :param old_letters: The letters that were already guessed
    :type old_letters: list
    :return: none
    :rtype: none
    """
    
    sort_old_letters = sorted(old_letters, key = str.lower)
    joined_old_letters = " -> ".join(sort_old_letters)
    
    print("X")
    print(joined_old_letters)

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Determines if the user input is legal.
    :param letter_guessed: The user's guess
    :param old_letters_guessed: The letters that were already guessed
    :type letter_guessed: list
    :type old_letters_guessed: list
    :return: A flag that returns true if the input is a single English letter and was not already given as an input, false for all other cases
    :rtype: bool
    """
    
    flag = False

    lower_guessed = letter_guessed.lower()
    
    if ((len(lower_guessed) == 1) and (lower_guessed in "abcdefghijklmnopqrstuvwxyz") and (lower_guessed not in old_letters_guessed)):
        flag = True
        old_letters_guessed.append(lower_guessed)

    if (flag == False):
        letter_sorter(old_letters_guessed)
    
    return (flag)

def check_win(secret_word, old_letters_guessed):
    """Checks all the old guesses the user made, and determines whether he has managed to guess all the letters in secret_word or not.
    :param secret_word: The word the user is trying to guess
    :param old_letters_guessed: The letters the user has already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return guess_string: A flag that returns true if the user has already managed to guess all the letters secret_word, false for all other cases
    :rtype: bool
    """
    count = 0

    flag = False
    
    for i in secret_word:
        if (i in old_letters_guessed):
            count += 1

    if (count >= len(secret_word)):
        flag = True
    
    return (flag)

def main():
    secret_word = ""
    old_letters_guessed = []
    MAX_TRIES = 6
    num_of_tries = 1

    win_flag = False

    print_welcome(MAX_TRIES)

    file_path = input("\nPlease enter the file path to your words: ")
    index = int(input("Please enter the index of your word: "))

    print("\nLet's start the game!")

    print_hangman(num_of_tries)

    secret_word = choose_word(file_path, index)

    print(show_hidden_word(secret_word, old_letters_guessed))

    while ((win_flag == False) and (num_of_tries != (MAX_TRIES + 1))):
        guessed_letter = input("\nGuess a letter: ").lower()

        check_valid_input_flag = check_valid_input(guessed_letter, old_letters_guessed)
        try_update_letter_guessed(guessed_letter, old_letters_guessed)

        if (check_valid_input_flag == False):
            continue

        elif (guessed_letter not in secret_word):
            print(":(")
            
            num_of_tries += 1
            print_hangman(num_of_tries)
            
            print(show_hidden_word(secret_word, old_letters_guessed))

        else:
            print(show_hidden_word(secret_word, old_letters_guessed))
            
        win_flag = check_win(secret_word, old_letters_guessed)

        if (win_flag == True):
            num_of_tries = MAX_TRIES + 1 #end the game prematurely

    if (win_flag == False):
        print("\nLOSE")
    else:
        print("\nWIN")

if __name__ == "__main__":
    main()
