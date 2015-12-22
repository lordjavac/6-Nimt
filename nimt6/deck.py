from .card_collection import CardCollection
from .card import Card

class Deck(CardCollection):
    """Initialize Deck and fill with Cards."""
    def __init__(self):
        super(Deck, self).__init__()
        for rank in range(1, 105):
            self.add(Card(rank))
