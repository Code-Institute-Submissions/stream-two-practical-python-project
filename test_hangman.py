import os
import unittest
import hangman


class TestHangman(unittest.TestCase):

    def test_get_word_from_dict(self):

        word = hangman.get_word()
        self.assertTrue(word, str)

    def test_is_word_is_more_than_4_letters(self):

        letter_list = hangman.word_is_more_than_four_letters()
        self.assertTrue(letter_list, str)
        self.assertTrue(len(letter_list), 3 )
        self.assertTrue(len(letter_list), 2 )
        self.assertTrue(len(letter_list), 1 )
        self.assertTrue(len(letter_list), 0 )
        self.assertTrue(len(letter_list), 9 )
        self.assertTrue(len(letter_list), 10 )
        