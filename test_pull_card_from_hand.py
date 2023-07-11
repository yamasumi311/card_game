from unittest import TestCase

from functions import pull_card_from_hand


class Test(TestCase):
    def test_pull_card_from_hand(self):
        cards = ['2-Heart', '3-spade']
        index = 0
        card, cards = pull_card_from_hand(cards, index)
        self.assertEqual(['3-spade'], cards)
        self.assertEqual('2-Heart', card)

    def test_pull_card_from_empty_hand(self):
        cards = []
        index = 0
        with self.assertRaises(IndexError):
            card, cards = pull_card_from_hand(cards, index)

    def test_pull_card_from_outside_of_hand(self):
        cards = ['2-Heart', '3-spade']
        index = 7
        with self.assertRaises(IndexError):
            card, cards = pull_card_from_hand(cards, index)
