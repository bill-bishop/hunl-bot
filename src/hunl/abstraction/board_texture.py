import numpy as np

class BoardTexture:
    """
    Computes simple board texture features:
    - Flush draw potential
    - Straight draw potential
    - Paired / monotone
    """

    @staticmethod
    def texture(board):
        suits = [c % 4 for c in board]
        ranks = [c // 4 for c in board]

        flush_potential = max(np.bincount(suits, minlength=4))
        paired = len(ranks) != len(set(ranks))
        straight_potential = BoardTexture._has_straight_draw(ranks)

        return np.array([
            flush_potential / len(board),
            float(paired),
            float(straight_potential)
        ], dtype=np.float32)

    @staticmethod
    def _has_straight_draw(ranks):
        ranks = sorted(set(ranks))
        for i in range(len(ranks) - 2):
            if ranks[i+2] - ranks[i] <= 4:
                return True
        return False
