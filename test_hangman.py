import os
import unittest
import random
import string
import tempfile
import doc_func
import logic
import game
import hangman

class TestHangman(unittest.TestCase):

    def test_write_to_file(self):
        file = tempfile.mkstemp()[1]
        data = "HELLO WORLD"

        try:
            doc_func.write_to_doc(file, data)
            content = open(file).read()
        finally:
            os.remove(file)

        self.assertEqual(content, data)

    def test_read_from_file(self):
        file = tempfile.mkstemp()[1]
        data = "HELLO WORLD"

        doc_func.write_to_doc(file, data)
        try:
            read_file = doc_func.read_doc(file)
        finally:
             os.remove(file)

        self.assertEqual(data, read_file)

    def test_write_username_and_current_word_to_file(self):
        username = "test"
        letter_list = "HELLO"

        file = tempfile.mkstemp()[1]
        doc_func.write_username_and_current_word_to_file(username, letter_list, file)

        try:
            read_file = open(file).read()  
        finally:
            os.remove(file)

        self.assertIn(username, read_file)
        self.assertIn(letter_list, read_file)


    def test_get_users_current_word_from_file(self):
        username = "test"
        letter_string = "WORD"
        file = tempfile.mkstemp()[1]

        doc_func.write_username_and_current_word_to_file(username, letter_string, file)

        try:
            read_file = doc_func.get_users_current_word(username, file)
        finally:
            os.remove(file)

        self.assertIn(letter_string, read_file)

    def test_write_guesses_to_file(self):
        username = "TEST"
        word = "WORD"
        current_word_file = tempfile.mkstemp()[1]
        guess = "(0, W)"

        doc_func.write_username_and_current_word_to_file(username, word, current_word_file)
        doc_func.write_guesses_to_current_word_file(username, word, current_word_file, guess)

        try:
            read_file = open(current_word_file).read()
            #print(read_file)
        finally:
            os.remove(current_word_file)

        self.assertIn(guess, read_file)

    def test_get_string_of_guess(self):
        check_guess = True
        guess = "W"
        word = "WORD"

        correct_guess = logic.get_string_of_guess(check_guess, guess, word)

        self.assertEqual(correct_guess, "(0, 'W')")
        self.assertIsInstance(correct_guess, str)


    def test_get_word_from_dict(self):
        word = logic.get_word()

        self.assertIsInstance(word, str)

    def test_letter_list_is_more_than_three_less_than_eleven(self):
        letters = logic.correct_length_letter_list()
        letters_length = int(len(letters))
        answer = ""
        if letters_length >= 4 and letters_length <= 10:
            answer = "correct number of letters"
        elif letters_length < 4:
            answer = "incorrect number of letters" 
        elif letters_length > 10:
            answer = "incorrect number of letters"
        
        self.assertEqual(answer, "correct number of letters")

        
    def test_create_alphabet_list(self):
        alphabet = logic.create_alphabet_list()

        i = "".join(alphabet)

        self.assertIsInstance(alphabet, list)
        self.assertIsInstance(i,str )
        self.assertTrue(i.isupper(), True)
        self.assertEqual(len(alphabet), 26)

    def test_is_guess_in_word(self):
        param = list("WORD")
        guesses = param
        word = param
        alphabet = list(string.ascii_uppercase)
        incorrect_letters = list(set(alphabet).difference(set(guesses)))

        for guess in guesses:
            guess_is_in = logic.is_guess_in_word(guess, word)
            self.assertEqual(guess_is_in, True)

        for guess in incorrect_letters:
            guess_not_in = logic.is_guess_in_word(guess, word)
            self.assertEqual(guess_not_in, False)
    
    def test_get_list_index_of_correct_guess(self):
        param = list("WORD")
        guesses = param
        word = param
        counter = -1

        for guess in guesses:
            get_list_number = logic.get_list_index_of_correct_guess(guess, word)
            counter += 1
            self.assertEqual(get_list_number, [(counter, guess)])

    def test_get_users_correct_guesses(self):
        username = "me"
        word = "WORD"
        guess = "(0, W)"
        current_word_file = tempfile.mkstemp()[1]
        guesses = "me_guesses:(0, W):;\n"

        doc_func.write_username_and_current_word_to_file(username, word, current_word_file)
        doc_func.write_guesses_to_current_word_file(username, word, current_word_file, guess)
       
        try:
            file_guesses = doc_func.get_users_correct_guesses(username, current_word_file)
        finally:
            os.remove(current_word_file)

        self.assertEqual(file_guesses, guesses)
        self.assertIn(guesses, file_guesses)
        self.assertEqual(type(file_guesses), str)

    def test_write_scores_to_file(self):
        username = "test"
        file = tempfile.mkstemp()[1]
        word = "WORD\n"
        
        doc_func.write_current_scores_to_file(username, file, word)
        try:
            read_file = open(file).read()
        finally:
            os.remove(file)
        self.assertIn("4", read_file)

    def test_get_current_user_score(self):
        file = tempfile.mkstemp()[1]
        username = "test"
        word = "WORD\n"
        doc_func.write_current_scores_to_file(username, file, word)

        try:
            read_file = doc_func.get_current_user_score(username, file)
        finally:
            os.remove(file)

            self.assertIn("4", read_file)

    def test_get_correct_guesses_list(self):
        correct_guesses = "me_guesses:(0, W):(1, O):;\n"

        number_of_guesses = logic.get_correct_guesses_list(correct_guesses)
        
        self.assertEqual(len(number_of_guesses), 2)
        self.assertIsInstance(len(number_of_guesses), int)

    def test_is_number_of_guesses_equal_to_current_word(self):
        word = "WORD"
        print(word)
        correct_guesses = "me_guesses:(0, W):(1, O)::(2, R)::(3, D):;\n"

        number_of_guesses = logic.get_correct_guesses_list(correct_guesses)
        number_of_guesses_length = len(number_of_guesses)
        guesses_equal_to_word = logic.are_number_of_guesses_equal_to_word(number_of_guesses_length, word)

        self.assertTrue(word, guesses_equal_to_word)
  
    def test_display_correct_guesses(self):
        word = "WORD\n"
        correct_guesses = "test_guesses:(0, 'W'):(1, 'O'):;"
        expected_display = ["W","O","_","_"]

        actual_display_guesses = logic.display_correct_guesses(word, correct_guesses)

        self.assertEqual(actual_display_guesses, expected_display )
    
    def test_write_incorrect_guess_counter_to_file(self):
        username = "test"
        file = tempfile.mkstemp()[1]
        counter = "10"
        letter_string = "WORD"

        doc_func.write_username_and_current_word_to_file(username, letter_string,file)
        doc_func.incorrect_guesses_counter_iterator(file, username)

        try:
            total_guesses = open(file).read()
        finally:
            os.remove(file)

        self.assertIn(counter,total_guesses)

    def test_get_incorrect_guesses_counter(self):
        username = "test"
        file = tempfile.mkstemp()[1]
        letter_string = "WORD"

        doc_func.write_username_and_current_word_to_file(username, letter_string,file)
    
        try:
            total_guesses = doc_func.get_incorrect_guesses_counter(file, username)
        finally:
            os.remove(file)

        self.assertEqual(total_guesses, 11)

    def test_set_image_id(self):
        incorrect_guess_count = 10
        expected_id = "image_{0}".format(incorrect_guess_count)
        image_id = logic.set_image_id(incorrect_guess_count) 

        self.assertEqual(image_id, expected_id)

    def test_get_scores_for_leaderboard(self):
        scores_file = "data/current_score.txt"
        sorted_scores = doc_func.get_scores_for_leaderboard(scores_file)

        self.assertTrue(sorted_scores, list)
        self.assertEqual(len(sorted_scores), 10)

########################### GAME LOOP FUNCTION TESTS #############################################

    def test_get_current_score_on_first_visit_to_user_game_page(self):
        username = "test"
        file = tempfile.mkstemp()[1]
        word = "WORD\n"
        
        doc_func.write_current_scores_to_file(username, file, word)
        try:
            current_score = game.get_current_score_on_first_visit_to_user_game_page(username)
        finally:
            os.remove(file)

        self.assertEqual(type(current_score), str)
       

    def test_generate_word(self):
        username = "test"
        file = tempfile.mkstemp()[1]

        guess_word = game.generate_word(username, file)

        self.assertEqual(type(guess_word), str )

    def test_results_object_for_front_end(self):
        display_correct_guess = []
        current_score = "22"
        are_total_correct_guesses_the_word = False
        image_id = "image_5"
        incorrect_guesses_count = "5"

        results_object = game.results_object_for_front_end(display_correct_guess, current_score, are_total_correct_guesses_the_word,image_id,incorrect_guesses_count)
        
        self.assertEqual(type(results_object), dict)
        self.assertEqual(results_object["displayGuess"], [])
        self.assertEqual(results_object["currentScore"], "22")
        self.assertEqual(results_object["win"], False)
        self.assertEqual(results_object["imageId"], "image_5")
        self.assertEqual(results_object["guessCount"], "5")
        
        
class ExpectedFailuretTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_clear_old_guesses_from_file(self):
        username = "me"
        word = "WORD"
        current_word_file = tempfile.mkstemp()[1]
        guess = "(0, W)"

        doc_func.write_username_and_current_word_to_file(username, word, current_word_file)
        doc_func.write_guesses_to_current_word_file(username, word, current_word_file, guess)
        doc_func.clear_old_guesses_from_file(username, current_word_file)

        try:
            read_file = open(current_word_file).read()
        finally:
            os.remove(current_word_file)

        self.assertIn(guess, read_file )
        

       

