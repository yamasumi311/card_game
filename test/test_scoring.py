from unittest import TestCase

from card_game.functions import scoring


class Test_scoring(TestCase):
    def test_scoring(self):
        my_score, co_score = scoring('higher', 0, 0)
        self.assertEqual(1, my_score)
        self.assertEqual(0, co_score)


    def test_scoring_2(self):
        result = scoring('higher', 0, 0)
        self.assertEqual((1, 0), result)


    def test_scoring_twice(self):
        my_score, co_score = scoring('higher', 0, 0)
        my_score, co_score = scoring('lower', 1, 0)
        self.assertEqual(1, my_score)
        self.assertEqual(1, co_score)
