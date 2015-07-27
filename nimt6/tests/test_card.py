import unittest

from 6nimt import Card

class TestCard(unittest.TestCase):
    def test_rank(self):
        for r in range(1,120):
            self.subTest(msg=None, i=r)
            c = Card(rank = r)
        pass

    def test_value(self):
        pass

if __name__ == '__main__':
    unittest.main()
