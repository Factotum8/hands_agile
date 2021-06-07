from unittest import TestCase

from game.points_calculator import PointsCalculator


class TestPointsCalculator(TestCase):
    test_cases = (
        (3, '12312..22..22..2', 2),
        (4, '1111999911119911', 1),
        (4, '1111111111111111', 0),
    )

    def test_calculate(self):
        for count, field, expect in self.test_cases:
            with self.subTest(field):
                self.assertEqual(expect, PointsCalculator(count, field).calculate())
