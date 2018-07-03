import os
import doc_func
import logic
import game
import json
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
    
################### MAIN RUN FILE ################################

###################### ROUTES #######################################
#####################################################################

@app.route("/", methods=["GET","POST"])
def index(): 
    username_message = ""
    if request.method=="POST":
        username = request.form["username"].lower()
        username_file = "data/usernames.txt"
        usernames = doc_func.read_doc(username_file)
        
        if username == "":
            username_message = "Please enter a username."
        elif username in usernames:
            username_message = "Username taken, enter an original username."
        else: 
            doc_func.write_to_doc(username_file, username + "\n")
            return redirect(username)
    return render_template("index.html", username_message=username_message)

@app.route("/<username>") 
def user(username):
    alphabet = logic.create_alphabet_list()
    current_score = game.get_current_score_on_first_visit_to_user_game_page(username)
    
    return render_template("game.html", username=username, alphabet=alphabet, score=current_score)

@app.route("/<username>/scores")
def scores(username):
    scores_file = "data/current_score.txt"
    top_scores = doc_func.get_scores_for_leaderboard(scores_file)
 
    return render_template("scores.html", username=username, top_scores=top_scores)

@app.route("/<username>/word")
def message(username):
    current_word_file = "data/current_word.txt"
    doc_func.clear_old_guesses_from_file(username, current_word_file)
    guess_word_json = game.generate_word(username, current_word_file)

    return guess_word_json

@app.route("/<username>/<guess_data>", methods=["GET","POST"])
def guess(username, guess_data): 
    if request.method=="POST":
        guess_results = game.play_game(username, guess_data)

    return guess_results
    
"""
if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)
"""

PORT = int(os.environ.get("PORT",5000))

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=PORT)


