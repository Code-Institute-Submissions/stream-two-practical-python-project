import os
import random
import string
import tempfile 
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

################## GLOBAL VARIABLES ################################

correct_guesses = []
guesses_counter = 8
score_counter = 0


################## DOCUMENT FUNCTIONS ###############################

def write_to_doc(file, data):
    
    with open(file, "a") as file:
        file.writelines(data)
        
def read_doc(file):
    
    with open(file, "r") as file:
        words = file.read()
    return words

def write_username_and_current_word_to_file(username, letter_list, file):
    
    current_word_file = file
    read_current_word_file = read_doc(current_word_file)
    write_data = "\n" + username + "\n" + username + "_" + "guesses;" + "\n" + letter_list + "\n"

    if username in read_current_word_file:
        with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                old_word = line
                new_word = letter_list
                break

        with open(current_word_file, 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_word, new_word  + "\n"))
    else:
        write_to_doc(current_word_file, write_data )

def clear_old_guesses_from_file(username, file):
    
    current_word_file = file
    read_current_word_file = read_doc(current_word_file)
    
    if username in read_current_word_file:
        with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_line = line
                split_line = line.split(",")
                new_line = split_line[0]
                print(old_line)
                print(split_line)
                print(new_line)
                break

        with open(current_word_file, 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_line, new_line))
    
    
def get_users_current_word(username, current_word_file):
     
    with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                word = line
                return word

def write_guesses_to_current_word_file(username, word, check_guess, current_word_file, guess):
    #correct_guess = ""

    if check_guess == True:
        correct_guess =  ', '.join(map(str, get_list_index_of_correct_guess(guess, word)))

        with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    print(username)
                    break
            for line in f:
                old_line = line
                split_line = line.split(";")
                print(split_line)
                new_line = split_line[0] + "," + correct_guess + ";" + "\n"
                print(new_line)
                break
              

        with open(current_word_file, 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(old_line, new_line))
    else:
        print("Guess not correct")

    return correct_guess
    
    


################# GAME LOGIC FUNCTIONS ##############################

def get_word():
    """ GET A WORD FROM THE WORD LIST """
    with open("data/words.txt","r") as words:
        word_list = words.read().split()
        word = random.choice(word_list).upper()
       # print(word)
    return word

def correct_length_letter_list():
    """ ONLY RETURN A LETTER LIST OF CERTAIN LENGHT """
    letter_list = list(get_word())
    is_correct_number_of_letters = len(letter_list)
        
    while is_correct_number_of_letters < 4 or is_correct_number_of_letters > 10:
        letter_list = list(get_word())
        is_correct_number_of_letters = len(letter_list)
        #print("the number of letters is {0} and word is {1}".format(is_correct_number_of_letters, letter_list))
        
    return letter_list
    
def make_list_of_length_word(letter_list,item):
    
    dashes_list = []
    letters = letter_list

    for i in letters:
        dashes_list.append(item)

    #print(dashes_list)
    #print(letters)
    return dashes_list


def create_alphabet_list():
    alphabet = list(string.ascii_uppercase)
   
    #print(alphabet)
    return alphabet

def is_guess_in_word(guess, word):

    if guess in word:
        return True
    else:
        return "Incorrect Guess"
    
def get_list_index_of_correct_guess(guess, word):
    
    number_word_list = list(enumerate(word, 0))

    letter_match = []
    for item in number_word_list:
        if guess == item[1]:
            letter_match.append(item)
    return letter_match


def join_correct_guesses_list(updated_list):
     
    joined_correct_guesses_list = " ".join(updated_list)

    return joined_correct_guesses_list


#def append_correct_guesses_list(correct_guess_list):
    
    #for item in correct_guess_list:
       # correct_guess_index = item[0]
       # correct_guess = item[1]
       # correct_guesses[correct_guess_index] = correct_guess

    #return correct_guesses

##### THIS FUNCTION NEEDS AMMENDING TO READ FROM FILE ########
#def if_check_guess_true(guess, word):
    
    #correct_guess_index = get_list_index_of_correct_guess(guess, word)

    ############ APPEND CORRECT GUESSES LIST - MUST BE IN A FILE NOT GLOBAL #######
    #update_correct_guesses_list = append_correct_guesses_list(correct_guess_index)
    ########### JOIN READ LIST FROM FILE #####################################
   # display_correct_guess = join_correct_guesses_list(update_correct_guesses_list)

   # print(guess)
   # print(display_correct_guess)
   # return display_correct_guess

############################################



    

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
        else: 
            write_to_doc(username_file, username + "\n")
            return redirect(username)
    return render_template("index.html", username_taken=username_taken)

@app.route("/<username>") 
def user(username):
    alphabet = create_alphabet_list()
    global score_counter
    score = score_counter
  
    return render_template("game.html", username=username, alphabet=alphabet, score=score)

@app.route("/<username>/scores")
def scores(username):
    #print(username)
    return render_template("scores.html", username=username)

@app.route("/<username>/word")
def message(username):
    current_word_file = "data/current_word.txt"
    letter_list = "".join(correct_length_letter_list())
    #clear_old_guesses_from_file(username, current_word_file)
    write_username_and_current_word_to_file(username, letter_list, current_word_file)
    

    return render_template("word.html", username=username, letter_list=letter_list, correct_guesses=correct_guesses)

@app.route("/<username>/<guess_data>", methods=["GET","POST"])
def guess(username, guess_data):
    #word = ""
    if request.method=="POST":
        current_word_file = "data/current_word.txt"
        guess = guess_data
        word = get_users_current_word(username, current_word_file)
        display_correct_guess = ""

        check_guess = is_guess_in_word(guess, word)
        write_guesses_to_current_word_file(username, word, check_guess, current_word_file, guess)

        ###### NEED TO PASS WORD IN FROM READ CURRENT WORD FILE #######
       

       # if check_guess == True:
           # display_correct_guess = if_check_guess_true(guess, word) 
        #else:
           # global correct_guesses
           # display_correct_guess = join_correct_guesses_list(correct_guesses)

        #if correct_guesses == word:
           # global score_counter
            #score_counter += 1
            #score = score_counter
            #print(score_counter)
            #return score_counter
           
    return render_template("guess.html", guess=guess, word=word, display_correct_guess=display_correct_guess)
    


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),port=os.getenv("PORT"), debug=True)


