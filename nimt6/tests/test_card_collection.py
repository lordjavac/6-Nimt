import unittest

from ..card_collection import CardCollection
from ..card import Card

class TestCardCollection(unittest.TestCase):
    """ Test the CardCollection base class. """
    def test_constructor(self):
        ''' Should produce an empty collection for cards. '''
        cc = CardCollection()
        self.assertEqual(len(cc), 0)

    def test_getitem_with_no_items(self):
        cc = CardCollection()
        with self.assertRaises(IndexError):
            cc[0]

    def test_getitem_with_item(self):
        cc = CardCollection()
        c = Card(1)
        cc.add(c)
        self.assertEqual(cc[0], c)

    def test_add_card(self):
        cc = CardCollection()
        c  = Card(1)
        cc.add(c)
        self.assertIn(c, cc)

    def test_add_non_card(self):
        cc = CardCollection()
        x = 1
        with self.assertRaises(TypeError):
            cc.add(x)

    def test_size_when_empty(self):
        cc = CardCollection()
        self.assertEqual(len(cc), 0)

    def test_size_with_contents(self):
        cc = CardCollection()
        for rank in range(1, 10):
            c = Card(rank)
            cc.add(c)
        self.assertEqual(len(cc), 9)

    def test_contains(self):
        ''' Should confirm if a given card is in the collction or not. '''
        cc = CardCollection()
        c1 = Card(1)
        c2 = Card(2)
        cc.add(c1)
        self.assertIn(c1, cc)
        self.assertNotIn(c2, cc)

    def test_iterator(self):
        ''' Should itterate over the contents of the collection. '''
        cc = CardCollection()

if __name__ == '__main__':
    unittest.main()
