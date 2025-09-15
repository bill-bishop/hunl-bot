class BetSizingSchemes:
    """
    Provides coarse and rich bet sizing sets per street.
    """

    COARSE = {
        "preflop": [2, 3, 4],
        "flop": [0.5, 1.0],
        "turn": [0.5, 1.0],
        "river": [0.75, 1.0]
    }

    RICH = {
        "preflop": [2, 2.5, 3, 4, 5],
        "flop": [0.25, 0.5, 0.75, 1.0, 2.0],
        "turn": [0.5, 0.75, 1.0, 2.0],
        "river": [0.5, 0.75, 1.0, 1.5, 2.0]
    }

    @staticmethod
    def get(street, rich=False):
        if rich:
            return BetSizingSchemes.RICH.get(street, [])
        return BetSizingSchemes.COARSE.get(street, [])
