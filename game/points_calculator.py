from collections import Counter


class PointsCalculator:
    """
    The class calculates win points for players.
    """

    blank_symbol = '.'

    def __init__(self, finger_count: int, game_field: str):
        self.finger_count = finger_count * 2
        self.game_field = self.prepare_field(game_field)
        self.appear_frequency = Counter(game_field)

    def prepare_field(self, game_field: str):
        """
        Remove dots from the game field. Expand the game field to one dimension list if it didn't.
        """
        return [int(i) for line in game_field for i in line if i != self.blank_symbol]

    def calculate(self) -> int:
        """
        The method calculates win points.
        """
        points = 0
        for frequency in self.appear_frequency.values():
            if frequency <= self.finger_count:
                points += 1
        return points
