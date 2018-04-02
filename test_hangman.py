import os
import unittest
import random
import string
import hangman


class TestHangman(unittest.TestCase):

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
        
        letter_list = hangman.correct_length_letter_list()
        dashes_list = hangman.make_dashes_list(letter_list)
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
        
        guesses = ["W","O","R","D"]
        word = "WORD"
        alphabet = list(string.ascii_uppercase)
        incorrect_letters = list(set(alphabet).difference(set(guesses)))

        for guess in guesses:
            guess_is_in = hangman.is_guess_in_word(guess, word)
            self.assertEqual(guess_is_in, guess)

        for guess in incorrect_letters:
            guess_not_in = hangman.is_guess_in_word(guess, word)
            self.assertEqual(guess_not_in, "Incorrect Guess")
        
        #self.assertNotIn(guess_letter_not_in, word)
        

        """
        word = ["H","A","N","G","M","A","N"]
        guesses = ["H","A","N","G","M","A","N"]
        alphabet = list(string.ascii_uppercase)
        incorrect_letters = list(set(alphabet).difference(set(guesses)))
        #print(guess_letter_not_in)

        for guess in guesses:
            guess_letter = hangman.is_guess_in_word(guess, word)

       # for guess in incorrect_letters:
           # guess_letter_not_in = hangman.is_guess_in_word(guess, word)


        self.assertIn(guess_letter, word)
        #self.assertNotIn(guess_letter_not_in, word)
        """