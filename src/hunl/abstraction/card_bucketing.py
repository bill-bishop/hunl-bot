import numpy as np
from sklearn.cluster import KMeans
from itertools import combinations
import pyspiel

class CardBucketer:
    """
    Buckets cards into clusters based on Expected Hand Strength (EHS).
    Uses k-means clustering on sampled hand equities.
    """

    def __init__(self, num_buckets=1000, num_samples=2000, seed=42):
        self.num_buckets = num_buckets
        self.num_samples = num_samples
        self.rng = np.random.default_rng(seed)
        self.kmeans = None

    def compute_equities(self, game, hands):
        """
        Approximate equities by simulating random boards.
        """
        equities = []
        for hand in hands:
            wins = 0
            total = 0
            for _ in range(self.num_samples):
                state = game.new_initial_state()
                # deal full board (Texas Hold'em has 5 public cards)
                while not state.is_terminal():
                    legal = state.legal_actions()
                    a = self.rng.choice(legal)
                    state.apply_action(a)
                returns = state.returns()
                wins += returns[0]
                total += 1
            equities.append(wins / max(1, total))
        return np.array(equities).reshape(-1, 1)

    def fit(self):
        game = pyspiel.load_game("universal_poker(betting=betting_nolimit_hunl, numPlayers=2)")
        deck = list(range(52))
        hands = list(combinations(deck, 2))
        self.rng.shuffle(hands)
        sample_hands = hands[: self.num_buckets * 2]

        X = self.compute_equities(game, sample_hands)
        self.kmeans = KMeans(n_clusters=self.num_buckets, random_state=0).fit(X)
        return self

    def bucket(self, hand):
        if self.kmeans is None:
            raise ValueError("Call fit() first")
        return int(self.kmeans.predict([[hand]])[0])


if __name__ == "__main__":
    bucketer = CardBucketer(num_buckets=10, num_samples=50)
    bucketer.fit()
    print("Bucketer trained with 10 buckets")
