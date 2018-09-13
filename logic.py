import string
import random  
################# GAME LOGIC FUNCTIONS ##############################

def get_word():
    """ GET A WORD FROM THE WORD LIST """
    with open("data/words.txt","r") as words:
        word_list = words.read().split()
        word = random.choice(word_list).upper()
    return word

def correct_length_letter_list():
    """ ONLY RETURN A LETTER LIST OF CERTAIN LENGHT """
    letter_list = list(get_word())
    is_correct_number_of_letters = len(letter_list)
        
    while is_correct_number_of_letters < 4 or is_correct_number_of_letters > 10:
        letter_list = list(get_word())
        is_correct_number_of_letters = len(letter_list)

    return letter_list
    
def make_list_of_length_word(word, item, correct_guesses):
    dashes_list = []
    for i in word:
       dashes_list.append(item)

    return dashes_list

def create_alphabet_list():
    """ MAKE LIST OF ALPHABET FOR UI SELECTION BUTTONS """
    alphabet = list(string.ascii_uppercase)
   
    return alphabet

def is_guess_in_word(guess, word):
    """ CHECK TO SEE IF THE CURRENT GUESS IS IN THE CURRENT WORD """
    if guess in word:
        return True
    else:
        return False
    
def get_list_index_of_correct_guess(guess, word):
    """ FIND OUT THE INDEX NUMBER OF THE CURRENT CORRECT GUESS """
    number_word_list = list(enumerate(word, 0))

    letter_match = []
    for item in number_word_list:
        if guess == item[1]:
            letter_match.append(item)
   
    return letter_match

def get_string_of_guess(check_guess, guess, word):
    """ CONVERT THE CORRECT GUESS LIST TO A STRING READY TO WRITE TO FILE """
    correct_guess = ""
    if check_guess == True:
        correct_guess =  ':'.join(map(str, get_list_index_of_correct_guess(guess, word)))
    else:
        print("Guess not correct")

    return correct_guess

def get_correct_guesses_list(correct_guesses):
    """ CONVERT READ CORRECT CORESSES FROM FILE TO LIST TO FIND OUT NUMBER OF CORRECT GUESSES"""
    correct_guesses_list = list(map(str, correct_guesses.split(":")))
    length_correct_guesses = len(correct_guesses_list)
    correct_guesses_list.pop(length_correct_guesses -1)
    correct_guesses_list.pop(0)

    return correct_guesses_list

def are_number_of_guesses_equal_to_word(number_of_correct_guesses, word):
    """ ARE THE NUMBER OF CORRECT GUESSES EQUAL TO THE WORD LENGTH, - 1 REMOVES CARRIAGE """
    word = (len(word) - 1)
    if number_of_correct_guesses == word:
        return True
    else:
        return False  

def display_correct_guesses(word, correct_guesses):
    word_list = list(word)
    word_length = len(word_list)
    word_list.pop((word_length) -1)
    correct_guesses = get_correct_guesses_list(correct_guesses)
    display_correct_guesses = []

    for i in word_list:
        display_correct_guesses.append("_")

    for i in correct_guesses:
        index = int(i[1])
        letter = i[5]
        display_correct_guesses[index] = letter

    return display_correct_guesses

def set_image_id(incorrect_guess_count):
    image_id = "image_{0}".format(incorrect_guess_count)

    return image_id