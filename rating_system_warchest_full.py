from rating_system_base import RatingSystem


class RatingSystemWarchest(RatingSystem):
    def default_rating(self) -> float:
        return 2000.0

    def get_win_eq(self, p1: float, p2: float) -> float:
        return 1 / (1 + 10 ** ((p2 - p1) / 1500))

    def get_points(self, winner_rating: float, looser_rating: float) -> (float, float):
        eq_winner = self.get_win_eq(winner_rating, looser_rating)
        change = 60 * (1 - eq_winner)
        cap = 5000 - winner_rating
        min_win = 5 if winner_rating > 4000 else 10
        winner_change = min(max(change, min_win), cap)
        loser_change = min(-change + 2, 0)

        return winner_change, loser_change

