
class Card:

    ten_points = ['J', 'Q', 'K', 'A']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def score(self):
        if self.rank in self.ten_points:
            return 10
        return int(self.rank)

    def __str__(self):
        return f'{self.suit}{self.rank}'

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)
