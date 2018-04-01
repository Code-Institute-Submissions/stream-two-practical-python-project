import os
import unittest
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