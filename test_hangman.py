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
        #print(answer)
        
        self.assertEqual(answer, "correct number of letters")

    def test_print_dashes_for_number_of_items_in_letter_list(self):

        string = "_" 
        letter_list = hangman.correct_length_letter_list()
        dashes_list = hangman.make_list_of_length_word(letter_list, string)
        dashes_length = len(dashes_list)
        letter_list_length = len(letter_list)
      
        """ IS A TUPLE RETURNED, IS THE DASHES LENGHT = TO LETTER LIST LENGTH """
        self.assertIsInstance(dashes_list, list)
        self.assertEqual(dashes_length, letter_list_length)
        
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
   
        

       

