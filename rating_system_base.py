from player import Player
import random


class RatingSystem:
    def default_rating(self) -> float:
        pass

    def get_win_eq(self, p1: float, p2: float) -> float:
        pass

    def get_points(self, winner_rating: float, looser_rating: float) -> (float, float):
        pass

    def play_game(self, p1: Player, p2: Player):
        p1_win_eq = self.get_win_eq(p1.power, p2.power)
        r = random.random()

        if p1_win_eq > r:
            self.change_rating(p1, p2)
        else:
            self.change_rating(p2, p1)

    def change_rating(self, winner: Player, loser: Player):
        winner_change, loser_change = self.get_points(winner.rating, loser.rating)
        winner.rating += winner_change
        loser.rating += loser_change




