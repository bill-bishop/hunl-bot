import math
from collections import defaultdict

class BayesianStats:
    """
    Tracks opponent action frequencies with Bayesian updates.
    Provides Wilson confidence intervals.
    """
    def __init__(self):
        self.counts = defaultdict(lambda: [0, 0])  # action -> [success, total]

    def update(self, action, success):
        self.counts[action][0] += success
        self.counts[action][1] += 1

    def mean(self, action):
        s, n = self.counts[action]
        return s / n if n > 0 else 0.0

    def wilson_ci(self, action, z=1.96):
        s, n = self.counts[action]
        if n == 0:
            return (0.0, 0.0)
        p = s / n
        denom = 1 + z**2 / n
        centre = p + z**2 / (2 * n)
        margin = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))
        return ((centre - margin) / denom, (centre + margin) / denom)
