from random import choice
from itertools import count


class Player:
    """ A "raw" player doesn't exist """

    _uid = count(0)

    def __init__(self):
        self.uid = next(self._uid)
        self.hand = []

    def set_hand(self, hand):
        self.hand = hand

    def get_score(self):
        score = 0
        for card in self.hand:
            score += card.score
        return score

    def play(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}_{self.uid}'


class Human(Player):
    """ Human player """
    def play(self):
        print(f'Your hand: {[str(e) for e in self.hand]}')
        print(f'Your score: {self.get_score()}')
        actions = ['hit', 'stay']
        decision = None
        while decision not in actions:
            decision = input(f'Choose and action {actions}: ')
        return decision


class RandomAI(Player):
    """ Random AI """
    def play(self):
        hand_display = '🂠 ' * len(self.hand)
        print(f'AI hand: {hand_display}')
        decision = choice(['stay', 'hit'])
        print(f'AI chose: {decision}')
        return decision


class IntelligentAI(Player):
    """  Build a custom AI """
    def play(self):
        # your code here
        pass
