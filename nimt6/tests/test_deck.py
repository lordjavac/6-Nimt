import unittest

from ..deck import Deck
from ..card import Card

class TestDeck(unittest.TestCase):
    """ Test the Deck class to verify that it functions properly. """
    def test_constructor(self):
        ''' Verify that the constructor fills the deck with cards. '''
        deck = Deck()
        self.assertEqual(len(deck), 104)

        # Check that all the cards are there.
        for r in range(1, 105):
            with self.subTest(msg=None):
                self.assertIn(Card(r), deck)

if __name__ == '__main__':
    unittest.main()
