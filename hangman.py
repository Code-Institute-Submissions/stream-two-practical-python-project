import os
import random
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

################## DOCUMENT FUNCTIONS ###############################

def write_to_doc(file, data):
    
    with open(file, "a") as file:
        file.writelines(data)

def get_word():
    """ GET A WORD FROM THE WORD LIST """
    with open("data/words.txt","r") as words:
        word_list = words.read().split()
        word = random.choice(word_list)
        #print(word)
    return word

#def make_letter_list():
    """ MAKE A LIST FROM THE RETURNED WORD """
    #letter_list = list(get_word())
    #print(letter_list)
    #return letter_list
   
def length_of_letter_list(letter_list):
    """ FIND THE LENGTH OF THE LETTER LIST PASSED FROM BELOW FUNCTION """
    number_of_letters = len(letter_list)
    #print(number_of_letters)
    return number_of_letters

def letter_list_is_more_than_three_less_than_eleven():
    
    letter_list = list(get_word())
    is_correct_number_of_letters = length_of_letter_list(letter_list)
   
    while is_correct_number_of_letters < 4 or is_correct_number_of_letters > 10:
        letter_list = list(get_word())
        is_correct_number_of_letters = length_of_letter_list(letter_list)
        
        #print(letter_list)
    
    print("the number of letters is {0} and word is {1}".format(is_correct_number_of_letters, letter_list))

    return letter_list
    
            
    

    



################# GAME LOGIC FUNCTIONS ##############################

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
    return render_template("game.html", username=username)

@app.route("/<username>/scores")
def scores(username):
    print(username)
    return render_template("scores.html", username=username)

@app.route("/<username>/message")
def message(username):
    message = "loser"
    return render_template("message.html", username=username, message=message)



if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)


