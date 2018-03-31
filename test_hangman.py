import os
import unittest
import hangman


class TestHangman(unittest.TestCase):

    def test_get_word_from_dict(self):

        word = hangman.get_word()
        self.assertIsInstance(word, str)
        self.assertTrue(len(word), 0)

    #def test_make_letters(self):
        
        #letters = hangman.make_letter_list()
        #for letter in letters:
            #return len(letter)

        #self.assertIsInstance(letters, list)
        #self.assertTrue(len(letters), 0)
        #self.assertTrue(letter, 0)
        
        
    #def test_letter_list_length_is_int(self, letter_list):


        #letters = hangman.length_of_letter_list(letter_list)

        #self.assertTrue(type(letters), int )

    def test_letter_list_is_more_than_three_less_than_eleven(self):
        
        letters = hangman.letter_list_is_more_than_three_less_than_eleven()
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
        
        