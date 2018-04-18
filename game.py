import doc_func
import logic
import json

########################### GAME LOOP FUNCTIONS #############################################

def get_current_score_on_first_visit_to_user_game_page(username):
    scores_file = "data/current_score.txt"
    current_score = doc_func.get_current_user_score(username, scores_file)

    if current_score == None: 
        current_score = ""
    else:
        current_score = doc_func.get_current_user_score(username, scores_file)

    return current_score

def generate_word(username, current_word_file):
    letter_list = logic.correct_length_letter_list()
    letter_string = "".join(letter_list)
    doc_func.write_username_and_current_word_to_file(username, letter_string, current_word_file)
    guess_word = {

        "guessWord":letter_list
    }
    guess_word_json = json.dumps(guess_word)
    ##print(letter_list)

    return guess_word_json
    
def get_correct_guesses_list_for_ui(username, current_word_file, word, check_guess):
    """ GET A LIST OF ALL CORRECT GUESSES """
    correct_guesses = doc_func.get_users_correct_guesses(username, current_word_file)
    make_list_of_guesses = logic.display_correct_guesses(word, correct_guesses) 

    return make_list_of_guesses

def iterate_and_return_failed_guesses_counter(current_word_file, username):
    """ ITERATE THE INCORRECT GUESSES COUNTER AND WRITE TO FILE, RETURN THE CURRENT SCORE """
    doc_func.incorrect_guesses_counter_iterator(current_word_file, username) 
    incorrect_guesses_count = doc_func.get_incorrect_guesses_counter(current_word_file, username)

    return incorrect_guesses_count

def has_the_user_guessed_correctly(username, current_word_file, word):
    """ HAS THE USER GUESSED CORRECTLY OVERALL, RETURN THE TRUE OR FALSE """
    correct_guesses = doc_func.get_users_correct_guesses(username, current_word_file)
    number_of_correct_guesses = len(logic.get_correct_guesses_list(correct_guesses))
    are_total_correct_guesses_the_word = logic.are_number_of_guesses_equal_to_word(number_of_correct_guesses, word)

    return are_total_correct_guesses_the_word

def if_the_letter_guess_is_correct_write_to_file(check_guess, guess, word, username, current_word_file):
    """ IF THE LETTER IS GUESSED CORRECTLY WRITE TO FILE """
    correct_guess = logic.get_string_of_guess(check_guess, guess, word)
    doc_func.write_guesses_to_current_word_file(username, word, current_word_file, correct_guess)

def results_object_for_front_end(display_correct_guess, current_score, are_total_correct_guesses_the_word,image_id,incorrect_guesses_count):
    results = {

        "displayGuess": display_correct_guess,
        "currentScore": current_score,
        "win": are_total_correct_guesses_the_word,
        "imageId":image_id,
        "guessCount": incorrect_guesses_count

    }
    return results

def if_guess_is_true(check_guess, current_word_file, username, word, guess, scores_file):
    incorrect_guesses_count = doc_func.get_incorrect_guesses_counter(current_word_file, username)
    image_id = logic.set_image_id(incorrect_guesses_count)
    current_score = doc_func.get_current_user_score(username, scores_file)

    if incorrect_guesses_count > 1:
        if_the_letter_guess_is_correct_write_to_file(check_guess, guess, word, username, current_word_file) 
        display_correct_guess = get_correct_guesses_list_for_ui(username, current_word_file, word, check_guess)
        are_total_correct_guesses_the_word = has_the_user_guessed_correctly(username, current_word_file, word) 
        if are_total_correct_guesses_the_word == True:
            doc_func.write_current_scores_to_file(username, scores_file, word)
            current_score = doc_func.get_current_user_score(username, scores_file)
    elif incorrect_guesses_count == 1:
        image_id = logic.set_image_id(incorrect_guesses_count) 

    results = results_object_for_front_end(display_correct_guess, current_score, are_total_correct_guesses_the_word,image_id,incorrect_guesses_count)

    return results

def if_guess_is_false(check_guess, current_word_file, username, word, guess, scores_file):
    are_total_correct_guesses_the_word = has_the_user_guessed_correctly(username, current_word_file, word)
    incorrect_guesses_count = doc_func.get_incorrect_guesses_counter(current_word_file, username)
    current_score = doc_func.get_current_user_score(username, scores_file)

    if incorrect_guesses_count > 1 and  are_total_correct_guesses_the_word == False:
        incorrect_guesses_count = iterate_and_return_failed_guesses_counter(current_word_file, username)
        image_id = logic.set_image_id(incorrect_guesses_count)
        display_correct_guess = get_correct_guesses_list_for_ui(username, current_word_file, word, check_guess)
    elif incorrect_guesses_count == 1:
        image_id = logic.set_image_id(incorrect_guesses_count)
        display_correct_guess = get_correct_guesses_list_for_ui(username, current_word_file, word, check_guess)
        
    results = results_object_for_front_end(display_correct_guess, current_score, are_total_correct_guesses_the_word,image_id,incorrect_guesses_count)
   
    return results

def overall_results_of_guess(current_word_file, username, word, guess, scores_file):
    check_guess = logic.is_guess_in_word(guess, word)
    if check_guess == True:
        results = if_guess_is_true(check_guess, current_word_file, username, word, guess, scores_file)             
    elif check_guess == False:
        results = if_guess_is_false(check_guess, current_word_file, username, word, guess, scores_file)

    return results

def play_game(username, guess_data):
    current_word_file = "data/current_word.txt"
    scores_file = "data/current_score.txt"
    guess = guess_data
    word = doc_func.get_users_current_word(username, current_word_file)
    doc_func.get_current_user_score(username, scores_file)

    results = overall_results_of_guess(current_word_file, username, word, guess, scores_file)
    results_json = json.dumps(results)

    return results_json