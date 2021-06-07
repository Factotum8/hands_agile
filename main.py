from game.points_calculator import PointsCalculator


def main() -> None:
    """
    Parse the keyboard input & call PointsCalculator
    """
    keys: int = int(input())
    desk: str = ''.join([input() for _ in range(4)])
    PointsCalculator(keys, desk)
    print(PointsCalculator(keys, desk).calculate(), end='')


if __name__ == '__main__':
    main()
