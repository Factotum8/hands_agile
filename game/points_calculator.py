from collections import Counter


class PointsCalculator:
    """
    The class calculates win points for players.
    """

    def __init__(self, finger_count: int, game_field: str):
        self.finger_count = finger_count * 2
        game_field = self.prepare_field(game_field)
        self.game_field = game_field
        self.appear_frequency = Counter(game_field)
        del self.appear_frequency['.']

    @staticmethod
    def prepare_field(game_field: str):
        """
        Remove dots from the game field & expand the game field to one dimension list.
        """
        return [int(i) for line in game_field for i in line if i != '.']

    def calculate(self) -> int:
        """
        The method calculates win points.
        """
        points = 0
        for _, frequency in self.appear_frequency.items():
            if frequency <= self.finger_count:
                points += 1
        return points
