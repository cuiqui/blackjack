from random import shuffle

import constants as c
from cards import Card


class Deck:

    def __init__(self):
        self.cards = self.make_french_deck()

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'

    def make_french_deck(self):
        return [Card(r, s) for s in c.SUITS for r in c.RANKS]

    def shuffle(self):
        shuffle(self.cards)

    def draw(self, quantity=1):
        hand = []
        try:
            for _ in range(quantity):
                hand.append(self.cards.pop())
        except IndexError:
            pass
        return hand
