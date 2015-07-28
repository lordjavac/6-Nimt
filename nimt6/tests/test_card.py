import unittest

from ..card import Card

class TestCard(unittest.TestCase):
    """ Test the cardclass to verify that it functions properly. """

    def test_rank(self):
        ''' Verify that we can create a card with a rank from 1 to 120. '''
        for i in range(104):
            rank = i + 1
            with self.subTest(rank=rank, msg=None):
                c = Card(rank = rank)
                self.assertEqual(c.rank, rank)

    def test_minimum_rank(self):
        ''' Verify that we can't create a card with a rank < 1. '''
        with self.assertRaises(ValueError):
            c = Card(rank = 0)

    def test_maximum_rank(self):
        ''' Verify that we cannot create a card with a rank > 104. '''
        with self.assertRaises(ValueError):
            c = Card(105)

    def test_value(self):
        ''' Verify that the values are computed properly. '''
        for i in range(104):
            rank = i + 1
            with self.subTest(rank=rank, msg=None):
                c = Card(rank = rank)

                if rank == 55:
                    self.assertEqual(c.value, 7, msg=None)
                elif rank % 11 == 0:
                    self.assertEqual(c.value, 5, msg=None)
                elif rank % 10 == 0:
                    self.assertEqual(c.value, 3, msg=None)
                elif rank % 5 == 0:
                    self.assertEqual(c.value, 2, msg=None)
                else:
                    self.assertEqual(c.value, 1, msg=None)

if __name__ == '__main__':
    unittest.main()
