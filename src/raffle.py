from random import randint

class Raffle(object):
    """


    """

    def __init__(self, previous_winner: str, current_week: str, raffle_candidates: list = []):
        self.previous_winner = previous_winner
        self. current_week = current_week
        self.raffle_candidates = raffle_candidates
        self.current_winner = None

    def select_winner(self):
        winner = raffle_candidates[randint(0, len(self.raffle_candidates) - 1)]
        self.current_winner = select_winner
        return winner
