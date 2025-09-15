import numpy as np

class ActionSpace:
    """
    Defines bet sizing schemes conditioned on SPR (stack-to-pot ratio).
    Provides masks for legal actions.
    """

    def __init__(self, sizes=None):
        # default bet sizes as pot fractions
        self.sizes = sizes or [0.25, 0.5, 1.0, 2.0]

    def get_bet_sizes(self, pot, stack):
        """
        Returns possible bet sizes given pot and stack.
        """
        bets = []
        for frac in self.sizes:
            bet = int(pot * frac)
            if bet < stack:
                bets.append(bet)
        if stack > 0:
            bets.append(stack)  # all-in always legal
        return np.unique(bets).tolist()

    def mask(self, legal_actions, action_dim):
        """
        Returns binary mask of legal actions.
        """
        mask = np.zeros(action_dim, dtype=np.float32)
        for a in legal_actions:
            mask[a] = 1.0
        return mask
