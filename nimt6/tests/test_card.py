import unittest

from ..card import Card

class TestCard(unittest.TestCase):
    """ Test the Card class to verify that it functions properly. """
    def test_rank(self):
        ''' Verify that we can create a card with a rank from 1 to 104. '''
        for r in range(1, 105):
            with self.subTest(msg=None):
                c = Card(rank = r)
                self.assertEqual(c.rank, r)

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
        for rank in range(1, 105):
            with self.subTest(msg=None):
                c = Card(rank)

                if rank == 55:
                    self.assertEqual(c.value, 7)
                elif rank % 11 == 0:
                    self.assertEqual(c.value, 5)
                elif rank % 10 == 0:
                    self.assertEqual(c.value, 3)
                elif rank % 5 == 0:
                    self.assertEqual(c.value, 2)
                else:
                    self.assertEqual(c.value, 1)

    def test_eq(self):
        ''' Verify that equality works correctly. '''
        self.assertTrue(Card(1) == Card(1))
        self.assertTrue(Card(100) == Card(100))
        self.assertFalse(Card(1) == Card(2))

    def test_lt(self):
        ''' Verify that the < operator works correctly. '''
        self.assertTrue(Card(1) < Card(2))
        self.assertFalse(Card(2) < Card(1))

    def test_gt(self):
        ''' Verify that the > operator works correctly. '''
        self.assertTrue(Card(2) > Card(1))
        self.assertFalse(Card(1) > Card(2))

if __name__ == '__main__':
    unittest.main()
