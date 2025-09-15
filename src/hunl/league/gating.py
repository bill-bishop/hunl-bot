import numpy as np

class Gating:
    """
    Promotes new policies to champion if they pass statistical tests.
    """
    def __init__(self, confidence=0.95, min_games=1000):
        self.confidence = confidence
        self.min_games = min_games

    def evaluate(self, results):
        """
        results: list of (reward_new - reward_old)
        """
        if len(results) < self.min_games:
            return False
        mean = np.mean(results)
        stderr = np.std(results) / np.sqrt(len(results))
        ci_low = mean - 1.96 * stderr
        return ci_low > 0
