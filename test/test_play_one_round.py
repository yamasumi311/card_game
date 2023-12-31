from unittest import TestCase

from functions import play_one_round


class Test_play_one_round(TestCase):
    def test_play_one_round(self):
        my_cards = ['2-Heart']
        co_cards = ['3-Spade']
        my_score = 0
        co_score = 0
        my_choice = 0
        co_choice = 0
        my_cards, co_cards, my_score, co_score = play_one_round(my_cards, co_cards, my_score, co_score, my_choice, co_choice)
        self.assertEqual([], my_cards)
        self.assertEqual([], co_cards)
        self.assertEqual(0, my_score)
        self.assertEqual(1, co_score)

    def test_play_one_round(self):
        my_cards = ['2-Heart', '5-dia']
        co_cards = ['3-Spade', '8-clover']
        my_score = 1
        co_score = 0
        my_choice = 1
        co_choice = 0
        my_cards, co_cards, my_score, co_score = play_one_round(my_cards, co_cards, my_score, co_score, my_choice,
                                                                co_choice)
        self.assertEqual(['2-Heart'], my_cards)
        self.assertEqual(['8-clover'], co_cards)
        self.assertEqual(2, my_score)
        self.assertEqual(0, co_score)
