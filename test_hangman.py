import os
import unittest
import random
import string
import tempfile 
import hangman

class TestHangman(unittest.TestCase):

    def test_write_to_file(self):
        file = tempfile.mkstemp()[1]
        data = "HELLO WORLD"

        try:
            hangman.write_to_doc(file, data)
            content = open(file).read()
        finally:
            os.remove(file)

        self.assertEqual(content, data)

    def test_read_from_file(self):
        file = tempfile.mkstemp()[1]
        data = "HELLO WORLD"

        hangman.write_to_doc(file, data)
        try:
            read_file = hangman.read_doc(file)
        finally:
             os.remove(file)

        self.assertEqual(data, read_file)

    def test_write_username_and_current_word_to_file(self):
        username = "test"
        letter_list = "HELLO"

        file = tempfile.mkstemp()[1]
        hangman.write_username_and_current_word_to_file(username, letter_list, file)

        try:
            read_file = open(file).read()  
        finally:
            os.remove(file)

        self.assertIn(username, read_file)
        self.assertIn(letter_list, read_file)


    def test_get_users_current_word_from_file(self):
        username = "test"
        letter_list = "WORD"
        file = tempfile.mkstemp()[1]

        hangman.write_username_and_current_word_to_file(username, letter_list, file)

        try:
            read_file = hangman.get_users_current_word(username, file)
        finally:
            os.remove(file)

        self.assertIn(letter_list, read_file)

    def test_write_guesses_to_file(self):
        username = "TEST"
        word = "WORD"
        current_word_file = tempfile.mkstemp()[1]
        guess = "(0, W)"

        hangman.write_username_and_current_word_to_file(username, word, current_word_file)
        hangman.write_guesses_to_current_word_file(username, word, current_word_file, guess)

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

        correct_guess = hangman.get_string_of_guess(check_guess, guess, word)

        self.assertEqual(correct_guess, "(0, 'W')")
        self.assertIsInstance(correct_guess, str)


    def test_get_word_from_dict(self):
        word = hangman.get_word()

        self.assertIsInstance(word, str)

    def test_letter_list_is_more_than_three_less_than_eleven(self):
        letters = hangman.correct_length_letter_list()
        letters_length = int(len(letters))
        answer = ""
        if letters_length >= 4 and letters_length <= 10:
            answer = "correct number of letters"
        elif letters_length < 4:
            answer = "incorrect number of letters" 
        elif letters_length > 10:
            answer = "incorrect number of letters"
        
        self.assertEqual(answer, "correct number of letters")

   # def test_print_dashes_for_number_of_items_in_letter_list(self):
       # string = "_" 
       # letter_list = hangman.correct_length_letter_list()
       # dashes_list = hangman.make_list_of_length_word(letter_list, string)
       # dashes_length = len(dashes_list)
       # letter_list_length = len(letter_list)
      
       # """ IS A TUPLE RETURNED, IS THE DASHES LENGHT = TO LETTER LIST LENGTH """
       # self.assertIsInstance(dashes_list, list)
       # self.assertEqual(dashes_length, letter_list_length)
        
    def test_create_alphabet_list(self):
        alphabet = hangman.create_alphabet_list()

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
            guess_is_in = hangman.is_guess_in_word(guess, word)
            self.assertEqual(guess_is_in, True)

        for guess in incorrect_letters:
            guess_not_in = hangman.is_guess_in_word(guess, word)
            self.assertEqual(guess_not_in, "Incorrect Guess")
    
    def test_get_list_index_of_correct_guess(self):
        param = list("WORD")
        guesses = param
        word = param
        counter = -1

        for guess in guesses:
            get_list_number = hangman.get_list_index_of_correct_guess(guess, word)
            counter += 1
            self.assertEqual(get_list_number, [(counter, guess)])

    def test_get_users_correct_guesses(self):
        username = "me"
        word = "WORD"
        guess = "(0, W)"
        current_word_file = tempfile.mkstemp()[1]
        guesses = "me_guesses:(0, W):;\n"

        hangman.write_username_and_current_word_to_file(username, word, current_word_file)
        hangman.write_guesses_to_current_word_file(username, word, current_word_file, guess)
       
        try:
            file_guesses = hangman.get_users_correct_guesses(username, current_word_file)
        finally:
            os.remove(current_word_file)

        self.assertEqual(file_guesses, guesses)
        self.assertIn(guesses, file_guesses)
        self.assertEqual(type(file_guesses), str)

    def test_write_scores_to_file(self):
        username = "test"
        file = tempfile.mkstemp()[1]
        word = "WORD\n"
        
        hangman.write_current_scores_to_file(username, file, word)
        try:
            read_file = open(file).read()
        finally:
            os.remove(file)
        self.assertIn("4", read_file)

    def test_get_current_user_score(self):
        file = tempfile.mkstemp()[1]
        username = "test"
        word = "WORD\n"
        hangman.write_current_scores_to_file(username, file, word)

        try:
            read_file = hangman.get_current_user_score(username, file)
        finally:
            os.remove(file)

            self.assertIn("4", read_file)

    def test_get_correct_guesses_list(self):
        correct_guesses = "me_guesses:(0, W):(1, O):;\n"

        number_of_guesses = hangman.get_correct_guesses_list(correct_guesses)
        
        self.assertEqual(len(number_of_guesses), 2)
        self.assertIsInstance(len(number_of_guesses), int)

    def test_is_number_of_guesses_equal_to_current_word(self):
        word = "WORD"
        print(word)
        correct_guesses = "me_guesses:(0, W):(1, O)::(2, R)::(3, D):;\n"

        number_of_guesses = hangman.get_correct_guesses_list(correct_guesses)
        number_of_guesses_length = len(number_of_guesses)
        guesses_equal_to_word = hangman.are_number_of_guesses_equal_to_word(number_of_guesses_length, word)

        self.assertTrue(word, guesses_equal_to_word)

    def test_if_guess_correct_message_to_user(self):
        are_total_guesses_the_word = True
        word = "WORD\n"
        win_message = "You are correct! You get {0} points.".format((len(word) -1))

        correct_guess = hangman.if_guessed_correct_message_to_user(are_total_guesses_the_word, word)

        self.assertEqual(correct_guess, win_message)
        self.assertIsInstance(correct_guess, str)

    def test_display_correct_guesses(word, correct_guesses):
        word = "WORD\n"
        correct_guesses = 


    """
    def test_correct_guesses_list_join(self):
        
        updated_list = list("WORDS")
        joined_list = hangman.join_correct_guesses_list(updated_list)

        self.assertEqual(joined_list, "W O R D S")
        self.assertIsInstance(joined_list, str)

    
    def test_append_guesses_list(self):

        hangman.correct_guesses = ["_","_","_","_"] 
        correct_guess_list = [(0, "W"),(1,"O")]
        appended_list = hangman.append_correct_guesses_list(correct_guess_list)

        self.assertIsInstance(appended_list, list)
        self.assertEqual(appended_list, ["W","O","_","_"])
    

    def test_if_check_guess_true(self):
        
        hangman.correct_guesses = ["_","_","_","_"] 
        guess = "W"
        word = list("WORD")

        if_check_guess_true = hangman.if_check_guess_true(guess, word)

        print(if_check_guess_true)

        self.assertIsInstance(if_check_guess_true, str)
        self.assertEqual(if_check_guess_true, "W _ _ _")
    """
   
class ExpectedFailuretTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_clear_old_guesses_from_file(self):
        username = "me"
        word = "WORD"
        current_word_file = tempfile.mkstemp()[1]
        guess = "(0, W)"

        hangman.write_username_and_current_word_to_file(username, word, current_word_file)
        hangman.write_guesses_to_current_word_file(username, word, current_word_file, guess)
        hangman.clear_old_guesses_from_file(username, current_word_file)

        try:
            read_file = open(current_word_file).read()
        finally:
            os.remove(current_word_file)

        self.assertIn(guess, read_file )
        

       

