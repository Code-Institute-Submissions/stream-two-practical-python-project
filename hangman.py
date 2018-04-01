import os
import random
import string
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

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
    
def make_dashes_list(letter_list):
    
    dashes_list = []
    letters = letter_list

    for i in letters:
        dashes_list.append("_")

    print(dashes_list)
    print(letters)
    return dashes_list

def create_alphabet_list():
    alphabet = list(string.ascii_uppercase)
   
    print(alphabet)
    return alphabet

def is_guess_in_word(data):
    guess = data[0]
    word = data[1]

    if any(guess(word)):
        print("{0} is in word".format(guess))
        correct_guess = guess
    else:
        print("{0} is NOT in {1}".format(guess, word))

    print("The word is {0}".format(word))
    return correct_guess


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
    dashes_list = make_dashes_list(letter_list)

    return render_template("word.html", username=username, letter_list = letter_list, dashes_list = dashes_list)

@app.route("/<username>/<data>", methods=["GET","POST"])
def guess(username, data):
    if request.method=="POST":
        print(data)

        guess = data[0]
        word = data[1]

        is_guess_in_word(data)

    return render_template("guess.html", guess=guess, word=word)
    


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)


