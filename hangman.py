import os
import random
import string
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

################## GLOBAL VARIABLES ################################

correct_guesses = []

################## DOCUMENT FUNCTIONS ###############################

def write_to_doc(file, data):
    
    with open(file, "a") as file:
        file.writelines(data)

################# GAME LOGIC FUNCTIONS ##############################

def get_word():
    """ GET A WORD FROM THE WORD LIST """
    with open("data/words.txt","r") as words:
        word_list = words.read().split()
        word = random.choice(word_list).upper()
        print(word)
    return word

def correct_length_letter_list():
    """ ONLY RETURN A LETTER LIST OF CERTAIN LENGHT """
    letter_list = list(get_word())
    is_correct_number_of_letters = len(letter_list)
        
    while is_correct_number_of_letters < 4 or is_correct_number_of_letters > 10:
        letter_list = list(get_word())
        is_correct_number_of_letters = len(letter_list)
        print("the number of letters is {0} and word is {1}".format(is_correct_number_of_letters, letter_list))
        
    return letter_list
    
def make_list_of_length_word(letter_list,item):
    
    dashes_list = []
    letters = letter_list

    for i in letters:
        dashes_list.append(item)

    print(dashes_list)
    print(letters)
    return dashes_list


def create_alphabet_list():
    alphabet = list(string.ascii_uppercase)
   
    print(alphabet)
    return alphabet

def is_guess_in_word(guess, word):

    if guess in word:
        return guess
    else:
        return "Incorrect Guess"
    
def get_list_number_of_correct_guess(guess, word):
    
    number_word_list = list(enumerate(word, 0))

    letter_match = []
    for item in number_word_list:
        if guess == item[1]:
            letter_match.append(item)
            
    print(letter_match)
    return letter_match


def join_correct_guesses_list(updated_list):
     
    joined_correct_guesses_list = " ".join(updated_list)

    return joined_correct_guesses_list

def append_correct_guesses_list(correct_guess_list):
    
    global correct_guesses

    for item in correct_guess_list:
        correct_guess_index = item[0]
        correct_guess = item[1]
        correct_guesses[correct_guess_index] = correct_guess

    return correct_guesses


###################### ROUTES #######################################
#####################################################################

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        write_to_doc("data/usernames.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route("/<username>") 
def user(username):
    alphabet = create_alphabet_list()
    return render_template("game.html", username=username, alphabet=alphabet)

@app.route("/<username>/scores")
def scores(username):
    print(username)
    return render_template("scores.html", username=username)

@app.route("/<username>/word")
def message(username):
    letter_list = correct_length_letter_list()
    dashes_list = make_list_of_length_word(letter_list, "")
    global correct_guesses
    correct_guesses = make_list_of_length_word(letter_list, " _ ")

    return render_template("word.html", username=username, letter_list=letter_list, dashes_list=dashes_list, correct_guesses=correct_guesses)

@app.route("/<username>/<guess_data>", methods=["GET","POST"])
def guess(username, guess_data):
    if request.method=="POST":
        #print(data)
        data = guess_data.split(",")
        guess = data[0]
        word = list(data[1])

        display_correct_guess=""

        check_guess = is_guess_in_word(guess, word)

        if check_guess == guess:
            correct_guess_list = get_list_number_of_correct_guess(guess, word)
            update_correct_guesses_list = append_correct_guesses_list(correct_guess_list)
            display_correct_guess = join_correct_guesses_list(update_correct_guesses_list)
        else:
            global correct_guesses
            display_correct_guess = join_correct_guesses_list(correct_guesses)
            #return display_correct_guess

            #make function to append correct guess based on list number to array of empty strings
    return render_template("guess.html", guess=guess, word=word, display_correct_guess=display_correct_guess)
    


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)


