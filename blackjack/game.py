import constants as c
from deck import Deck
from player import Human, RandomAI


class Game:
    def __init__(self):
        self.deck = None
        self.players = None
        self.scores = None
        self.rounds_left = None
        self.game_over = False

    def new(self):
        self.game_over = False
        self.rounds_left = c.ROUNDS
        self.players = [Human(), RandomAI()]
        self.scores = {str(k): 0 for k in self.players}
        self.new_round()

    def new_round(self):
        self.deck = Deck()
        self.deck.shuffle()
        for player in self.players:
            player.hand = []
            self.deal(player=player, quantity=2)

    def deal(self, player, quantity=1):
        for card in self.deck.draw(quantity):
            player.hand.append(card)

    def turn(self, player):
        score = None
        action = player.play()
        if action == 'hit':
            self.deal(player)
            if player.get_score() > c.POINTS:
                score = 0
        elif action == 'stay':
            score = player.get_score()
        return score

    def balance(self, scores):
        print('----- Scores -----')
        print(f'Round scores (points made in round): {scores}')

        tie = True
        winner = scores.popitem()
        for k, v in scores.items():
            if v > winner[1]:
                winner = (k, v)
                tie = False
            elif v < winner[1]:
                tie = False

        if not tie:
            self.scores[winner[0]] += 1

        print(f'General scores (rounds won by each): {self.scores}')

    def run(self):
        # while there are still rounds left
        while self.rounds_left:
            # set round scores to empty
            scores = {}

            # for each player, do a whole turn, which can involve
            # multiple actions, i.e., two or more "hits"
            for player in self.players:
                print(f'---- {str(player)} turn ----')

                # turn is not over until we receive a score,
                # whether it's 0, which means it overstepped
                # or 0 < x <= 21
                turn_over = False
                while not turn_over:

                    # do a turn until we get a score, if we don't
                    # have a score, that means that the engine
                    # "hit" and didn't overstepped, so it's still
                    # its turn.
                    score = self.turn(player)
                    if score is not None:
                        print(f'Hand: {[str(e) for e in player.hand]}, points: {player.get_score()}')

                        # store scores for this player in this round
                        # and hand control over
                        scores[str(player)] = score
                        turn_over = True

            # do a balance after finishing round
            self.balance(scores)

            # begin new round and reduce rounds left by 1
            self.new_round()
            self.rounds_left -= 1
            print(f'Rounds left: {self.rounds_left}')


if __name__ == '__main__':
    g = Game()
    g.new()
    g.run()
