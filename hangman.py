import os
import random
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

################## DOCUMENT FUNCTIONS ###############################

def write_to_doc(file, data):
    with open(file, "a") as file:
        file.writelines(data)


def get_word():
    with open("data/words.txt","r") as words:
        word_list = words.read().split()
        word = random.choice(word_list)
        print(word)
    return word

def word_is_more_than_four_letters():
    
    letter_list = list(get_word())
    print(letter_list)
    while len(letter_list) < 4:
        letter_list = list(get_word())
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


