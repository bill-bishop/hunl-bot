import numpy as np

class MixPolicy:
    """
    λ-mix between GTO (blueprint) policy and exploitative policy.
    """
    def __init__(self, gto_policy, exploiter_policy, lam=0.5):
        self.gto = gto_policy
        self.exploiter = exploiter_policy
        self.lam = lam

    def act(self, obs):
        gto_probs = self.gto(obs)
        exp_probs = self.exploiter(obs)
        mix = self.lam * gto_probs + (1 - self.lam) * exp_probs
        mix /= np.sum(mix)
        return np.random.choice(len(mix), p=mix)
