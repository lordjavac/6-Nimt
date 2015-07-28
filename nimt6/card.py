class Card(object):
    """Represents a card in the 6 nimt game"""
    def __init__(self, rank):
        if rank <= 0 or rank > 104:
            raise ValueError('rank must be between 1 and 104 inclusive')

        super(Card, self).__init__()
        self.rank = rank

        if rank == 55:
            self.value = 7
        elif rank % 11 == 0:
            self.value = 5
        elif rank % 10 == 0:
            self.value = 3
        elif rank % 5 == 0:
            self.value = 2
        else:
            self.value = 1
