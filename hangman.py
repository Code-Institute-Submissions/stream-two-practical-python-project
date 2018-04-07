import os
import random
import string
import tempfile 
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

def write_username_and_current_word_to_file(username, letter_list, file):
    read_current_word_file = read_doc(file)
    #write_data = "\n" + username + "\n" + username + "_" + "guesses:;" + "\n" + letter_list + "\n"
    write_data = "\n{0}\n{1}_guesses:;\n{2}\n10\n".format(username, username, letter_list)
    if username in read_current_word_file:
        print(username)
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                old_word = line
                new_word = letter_list
                break
        
            
        with open(file, 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_word, new_word  + "\n"))
            
    else:
        write_to_doc(file, write_data)

def test(username, file):
    read_current_word_file = read_doc(file)
    #write_data = "\n{0}\n{1}_guesses:;\n{2}\n10\n".format(username, username, letter_list)
    if username in read_current_word_file:
        print(username)
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                break
            for line in f:
                print(line)
                old_counter = line
                new_counter = "10\n"
                break

        with open(file, 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_counter, new_counter))
    #else:
        #write_to_doc(file, write_data)


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
                #new_line = split_line[0] + correct_guess + ":;" + "\n"
                new_line = "{0}{1}:;\n".format(split_line[0], correct_guess)
                
                with open(current_word_file, 'r+') as f:
                    content = f.read()
                    f.seek(0)
                    f.truncate()
                    f.write(content.replace(old_line, new_line))
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
                #new_line = username + "_" + "guesses:;" + "\n"
                new_line = "{0}_guesses:;\n".format(username)
                break

        with open(file, 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_line, new_line))


def get_users_correct_guesses(username, file):
    with open(file, "r") as f:
        for line in f:
            if username in line:
                break
        for line in f:
            guesses = line
            #print(guesses)
            break
    return guesses

def write_current_scores_to_file(username, file, word):
    scores_file = read_doc(file)
    word_length = len(word)
    word_score = word_length - 1
    print(word)

    if username in scores_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_score = line
                old_score_to_int = int(old_score)
                new_score_sum = old_score_to_int + word_score
                new_score = "{0}\n".format(new_score_sum)
                break
        
        with open(file, "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_score, new_score))
    else:
        write_to_doc(file, "{0}\n{1}\n".format(username, word_score))

def get_current_user_score(username, file):
    scores_file = read_doc(file)

    if username in scores_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                current_score = line

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
                incorrect_guesses = line
                incorrect_guesses_int = int(incorrect_guesses)
                incorrect_guesses_int -= 1
                new_incorrect_guesses = str(incorrect_guesses_int)
                break

        with open(current_word_file, "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(incorrect_guesses, new_incorrect_guesses + "\n"))


    
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
    #print(letter_match)
    return letter_match

def get_string_of_guess(check_guess, guess, word):
    """ CONVERT THE CORRECT GUESS LIST TO A STRING READY TO WRITE TO FILE """
    correct_guess = ""
    #print(guess)
    if check_guess == True:
        correct_guess =  ':'.join(map(str, get_list_index_of_correct_guess(guess, word)))
        #print(correct_guess)
    else:
        print("Guess not correct")

    return correct_guess

def get_correct_guesses_list(correct_guesses):
    """ CONVERT READ CORRECT CORESSES FROM FILE TO LIST TO FIND OUT NUMBER OF CORRECT GUESSES"""
    correct_guesses_list = list(map(str, correct_guesses.split(":")))
    length_correct_guesses = len(correct_guesses_list)
    correct_guesses_list.pop(length_correct_guesses -1)
    correct_guesses_list.pop(0)
   # print(len(correct_guesses_list))

    return correct_guesses_list

def are_number_of_guesses_equal_to_word(number_of_correct_guesses, word):
    """ ARE THE NUMBER OF CORRECT GUESSES EQUAL TO THE WORD LENGTH, - 1 REMOVES CARRIAGE """
    word = (len(word) - 1)
    
    if number_of_correct_guesses == word:
        return True
    else:
        return False  

def if_guessed_correct_message_to_user(are_total_correct_guesses_the_word, word):
    if are_total_correct_guesses_the_word == True:
        win_message = "You are correct! You get {0} points.".format((len(word) - 1))

        return win_message

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
    


###################### ROUTES #######################################
#####################################################################

@app.route("/", methods=["GET","POST"])
def index(): 
    username_taken = ""
    if request.method=="POST":
        username_file = "data/usernames.txt"
        username = request.form["username"].lower()
        usernames = read_doc(username_file)
        
        if username in usernames:
            print("username taken")
            username_taken = "Username taken, please think of an original username."
            ########## write option continue old game #############
        else: 
            write_to_doc(username_file, username + "\n")
            return redirect(username)
    return render_template("index.html", username_taken=username_taken)

@app.route("/<username>") 
def user(username):
    alphabet = create_alphabet_list()
    
    return render_template("game.html", username=username, alphabet=alphabet)

@app.route("/<username>/scores")
def scores(username):
    return render_template("scores.html", username=username)

@app.route("/<username>/word")
def message(username):
    current_word_file = "data/current_word.txt"
    letter_list = "".join(correct_length_letter_list())
    clear_old_guesses_from_file(username, current_word_file)
    write_username_and_current_word_to_file(username, letter_list, current_word_file)
    test(username, current_word_file)

    return render_template("word.html", username=username, letter_list=letter_list)

@app.route("/<username>/<guess_data>", methods=["GET","POST"])
def guess(username, guess_data): 
    if request.method=="POST":
        current_word_file = "data/current_word.txt"
        scores_file = "data/current_score.txt"
        guess = guess_data
        word = get_users_current_word(username, current_word_file)
        display_correct_guess = ""
        win_message = ""
        current_score = ""

        check_guess = is_guess_in_word(guess, word)
        if check_guess == False:
            incorrect_guesses_counter_iterator(current_word_file, username) 
        else:
            correct_guess = get_string_of_guess(check_guess, guess, word)
            write_guesses_to_current_word_file(username, word, current_word_file, correct_guess)
            correct_guesses = get_users_correct_guesses(username, current_word_file)
            number_of_correct_guesses = len(get_correct_guesses_list(correct_guesses))
            are_total_correct_guesses_the_word = are_number_of_guesses_equal_to_word(number_of_correct_guesses, word)
            win_message = if_guessed_correct_message_to_user(are_total_correct_guesses_the_word, word)

            if are_total_correct_guesses_the_word == True:
                write_current_scores_to_file(username, scores_file, word)
                current_score = get_current_user_score(username, scores_file)
                display_correct_guess = display_correct_guesses(word, correct_guesses)


        ######### CREATE GUESSES COUNTER, MINUS GUESS FOR INCORRECT GUESS, DISPLAY CSS IMAGE BASED ON COUNTER NUMBER, USE PYTHON 
        ########## TO CHANGE ID OF HTML ID FOR IMAGE, SO CHANGING WHICH CSS FILE IS LOADED ############
        ######### CREATE SCORE BOARD, SEARCH FOR TOP 10 SCORES, PULL USERNAME AND SCORE PAIRS INTO TABLE #############

           
    return render_template("guess.html", guess=guess, word=word, display_correct_guess=display_correct_guess, win_message=win_message, current_score=current_score)
    


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)


