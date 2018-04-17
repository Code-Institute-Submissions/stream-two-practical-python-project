import os
import random
import string
import tempfile 
import time
import operator
import json
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

################## DOCUMENT FUNCTIONS ###############################

def write_to_doc(file, data):
    with open(file, "a") as file:
        file.writelines(data)
        
def read_doc(file):
    with open(file, "r") as file:
        words = file.read()
    return words

def read_and_replace(file, old, new):    
    with open(file, 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace(old, new))
        f.close
    
def write_username_and_current_word_to_file(username, letter_string, file):
    read_current_word_file = read_doc(file)
    write_data = "\n{0}\n{1}_guesses:;\n{2}\n{3}_fail_count:11:\n".format(username, username, letter_string, username)
    if username in read_current_word_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                old_word = line
                new_word = letter_string
                break
            for line in f:
                print(line)
                old_counter = line
                new_counter = "{0}_fail_count:11:\n".format(username)
                break
        read_and_replace(file, old_word, new_word + "\n")
        read_and_replace(file, old_counter, new_counter) 
    else:
        write_to_doc(file, write_data)

def get_users_current_word(username, file):
    with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                word = line
                return word

def write_guesses_to_current_word_file(username, word, current_word_file, correct_guess):
    with open(current_word_file, "r") as f:
        for line in f:
            if username in line:
                break
        for line in f:
            if correct_guess not in line:
                old_line = line
                split_line = line.split(";")
                new_line = "{0}{1}:;\n".format(split_line[0], correct_guess)
                read_and_replace(current_word_file, old_line, new_line)
                break
            else:
                print("Already guessed {0}".format(correct_guess))    
                break
        
def clear_old_guesses_from_file(username, file):
    read_current_word_file = read_doc(file)
    if username in read_current_word_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_line = line
                new_line = "{0}_guesses:;\n".format(username)
                break

        read_and_replace(file, old_line, new_line)
    
def get_users_correct_guesses(username, file):
    with open(file, "r") as f:
        for line in f:
            if username in line:
                break
        for line in f:
            guesses = line
            break
    return guesses

def write_current_scores_to_file(username, file, word):
    scores_file = read_doc(file)
    word_length = len(word)
    word_score = word_length - 1

    if username in scores_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_score = line
                old_score_list = list(map(str, old_score.split(":")))
                old_score_to_int = int(old_score_list[2])
                new_score_sum = old_score_to_int + word_score
                new_score = ":{0}:{1}:\n".format(username, new_score_sum)
                break
        read_and_replace(file, old_score, new_score)
    else:
        write_to_doc(file, "\n:{0}\n:{1}:{2}:\n".format(username, username, word_score))

def get_current_user_score(username, file):
    scores_file = read_doc(file)
    if username in scores_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_score = line
                old_score_list = list(map(str,old_score.split(":")))
                current_score = old_score_list[2]
                break  

            return current_score

def incorrect_guesses_counter_iterator(current_word_file, username):
    read_current_word_file = read_doc(current_word_file)
    if username in read_current_word_file:
        with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                break
            for line in f:
                old_count = line
                old_count_list = list(map(str,old_count.split(":")))
                counter = int(old_count_list[1])
                if counter >= 0:
                    counter -= 1
                set_new_count = old_count_list
                set_new_count[1] = str(counter)
                new_count = ":".join(set_new_count)
                break

        read_and_replace(current_word_file, old_count, new_count)

def get_incorrect_guesses_counter(current_word_file, username):
    read_current_word_file = read_doc(current_word_file)
    if username in read_current_word_file:
        with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                break
            for line in f:
                incorrect_list = list(map(str, line.split(":")))
                incorrect_count = int(incorrect_list[1])
                print(incorrect_count)
                break

            return incorrect_count

def get_scores_for_leaderboard(scores_file):
    with open(scores_file, "r") as f:
        all_scores = []
        scores_line = list(f)[2::3]
        for i in scores_line:
            scores_list = list(map(str, i.split(":")))
            scores_list.pop(0)
            scores_list.pop(2)
            scores_list[1] = int(scores_list[1])
            all_scores.append(scores_list)
        all_scores.sort(key=operator.itemgetter(1), reverse=True)

        return all_scores[:10]
    
################# GAME LOGIC FUNCTIONS ##############################

def get_word():
    """ GET A WORD FROM THE WORD LIST """
    with open("data/words.txt","r") as words:
        word_list = words.read().split()
        word = random.choice(word_list).upper()
        #print(word)
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
    
###################### ROUTES #######################################
#####################################################################

@app.route("/", methods=["GET","POST"])
def index(): 
    username_message = ""
    if request.method=="POST":
        username_file = "data/usernames.txt"
        username = request.form["username"].lower()
        usernames = read_doc(username_file)
        
        if username == "":
            username_message = "Please enter a username."
        elif username in usernames:
            username_message = "Username taken, enter an original username."
        else: 
            write_to_doc(username_file, username + "\n")
            return redirect(username)
    return render_template("index.html", username_message=username_message)

@app.route("/<username>") 
def user(username):
    alphabet = create_alphabet_list()
    scores_file = "data/current_score.txt"
    current_score = get_current_user_score(username, scores_file)

    if current_score == None: 
        current_score = ""
    else:
        current_score = get_current_user_score(username, scores_file)
        
    return render_template("game.html", username=username, alphabet=alphabet, score=current_score)

@app.route("/<username>/scores")
def scores(username):
    scores_file = "data/current_score.txt"
    top_scores = get_scores_for_leaderboard(scores_file)
 
    return render_template("scores.html", username=username, top_scores=top_scores)

@app.route("/<username>/word")
def message(username):
    current_word_file = "data/current_word.txt"
    letter_list = correct_length_letter_list()
    letter_string = "".join(letter_list)
    clear_old_guesses_from_file(username, current_word_file)
    write_username_and_current_word_to_file(username, letter_string, current_word_file)

    guess_word = {

        "guessWord":letter_list
    }

    guess_word_json = json.dumps(guess_word)

    return guess_word_json

@app.route("/<username>/<guess_data>", methods=["GET","POST"])
def guess(username, guess_data): 
    if request.method=="POST":
        current_word_file = "data/current_word.txt"
        scores_file = "data/current_score.txt"
        guess = guess_data
        word = get_users_current_word(username, current_word_file)
        current_score = ""
        image_id = ""

        check_guess = is_guess_in_word(guess, word)
        correct_guesses = get_users_correct_guesses(username, current_word_file)
        display_correct_guess = display_correct_guesses(word, correct_guesses)
        current_score = get_current_user_score(username, scores_file)
    
        if check_guess == True:
            incorrect_guesses_count = get_incorrect_guesses_counter(current_word_file, username)
            image_id = set_image_id(incorrect_guesses_count)
            if incorrect_guesses_count > 1:
                correct_guess = get_string_of_guess(check_guess, guess, word)
                write_guesses_to_current_word_file(username, word, current_word_file, correct_guess)
                correct_guesses = get_users_correct_guesses(username, current_word_file)
                display_correct_guess = display_correct_guesses(word, correct_guesses)   
                number_of_correct_guesses = len(get_correct_guesses_list(correct_guesses))
                are_total_correct_guesses_the_word = are_number_of_guesses_equal_to_word(number_of_correct_guesses, word)

                if are_total_correct_guesses_the_word == True:
                    write_current_scores_to_file(username, scores_file, word)
                    current_score = get_current_user_score(username, scores_file)

            elif incorrect_guesses_count == 1:
                image_id = set_image_id(incorrect_guesses_count) 
                 
        elif check_guess == False:
            number_of_correct_guesses = len(get_correct_guesses_list(correct_guesses))
            are_total_correct_guesses_the_word = are_number_of_guesses_equal_to_word(number_of_correct_guesses, word)
            incorrect_guesses_count = get_incorrect_guesses_counter(current_word_file, username)

            if incorrect_guesses_count > 1 and  are_total_correct_guesses_the_word == False:
                incorrect_guesses_counter_iterator(current_word_file, username) 
                incorrect_guesses_count = get_incorrect_guesses_counter(current_word_file, username)
                image_id = set_image_id(incorrect_guesses_count)
                correct_guesses = get_users_correct_guesses(username, current_word_file)
                display_correct_guess = display_correct_guesses(word, correct_guesses)
            elif incorrect_guesses_count == 1:
                correct_guesses = get_users_correct_guesses(username, current_word_file)
                display_correct_guess = display_correct_guesses(word, correct_guesses)

                image_id = set_image_id(incorrect_guesses_count)

        results = {
            
            "displayGuess": display_correct_guess,
            "currentScore": current_score,
            "win": are_total_correct_guesses_the_word,
            "imageId":image_id,
            "guessCount": incorrect_guesses_count

        }

        results_json = json.dumps(results)

    return results_json
    
"""
if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)

"""
port = int(os.environ.get("PORT",5000))
##host = int(os.environ.get("IP",0.0.0.0))

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port = port)
