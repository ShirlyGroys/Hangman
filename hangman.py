# Hangman game. Try to guess the word :)

HANGMAN_ASCII_ART = ("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")


HANGMAN_PHOTOS = {1: "x-------x", 2: """x-------x
    |
    |
    |
    |
    |

""", 3: """
    x-------x
    |       |
    |       0
    |
    |
    |

""", 4:("""    x-------x
|       |
|       0
|       |
|
|

"""), 5: """        x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 6: """        x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

""", 7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}



def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):                # Returns the secret word from file
    file = open(file_path, "rt")
    data = file.read()
    word = data.split()
    lines = data.splitlines()
    uniques = set()
    for line in lines:
        uniques |= set(line.split())
    return (word[index])


def check_valid_input(letter_guessed, old_letters_guessed):         # checks if the guessed letter wasn't guessed before & is correct
    if letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):     # checks if your letter was guessed before, and appends to the guessed letters list
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print(":(" + " These are the letters that you have guessed already:")
        print(old_letters_guessed)
        return False


def show_hidden_word(secret_word, old_letters_guessed):         # converting letters from your secret words to lines
    secret_word_list = list(secret_word)
    for n, i in enumerate(secret_word_list):
        if i in old_letters_guessed:
            continue
        else:
            secret_word_list[n] = ' _ '
    print(''.join(secret_word_list))



def check_win(secret_word, old_letters_guessed):                  # checks if youv'e guessed your word
    secret_word_list = list(secret_word)
    if set(secret_word_list) <= set(old_letters_guessed):
        print("You've guessed the word :)")
        return True
    else:
        return False


def play_game():
    MAX_TRIES = 7
    num_of_tries = 1
    print(HANGMAN_ASCII_ART)
    get_path = "hangman.txt"
    index_path = int(input("Enter a number for index:"))
    secret_word = choose_word(get_path, index_path)
    old_letters_guessed = []
    while True:
        choose_a_letter = (input("guess a letter: "))
        try_update_letter_guessed(choose_a_letter,  old_letters_guessed)
        if choose_a_letter not in secret_word:
            num_of_tries += 1
            print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters_guessed)
        if check_win(secret_word, old_letters_guessed):
            return False
        if num_of_tries == MAX_TRIES:
            print("you lost the game!")
            break


if __name__ == "__main__":
    play_game()