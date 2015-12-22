from .card import Card

class CardCollection(object):
    """ Creates a collection of cards """
    def __init__(self):
        super(CardCollection, self).__init__()
        self._cards = list()

    def add(self, card):
        if  not isinstance(card, Card):
            raise TypeError('Only Cards may be added to a CardCollection.')
        self._cards.append(card)

    def __len__(self):
        return len(self._cards)

    def __contains__(self, object):
        return object in self._cards

    def __getitem__(self, index):
        return self._cards[index]
