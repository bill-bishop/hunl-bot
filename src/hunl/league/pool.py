import random

class OpponentPool:
    """
    Manages a pool of opponent policies (blueprints, exploiters, etc.).
    """
    def __init__(self):
        self.policies = {}

    def add(self, name, policy):
        self.policies[name] = policy

    def sample(self, strategy="uniform"):
        if not self.policies:
            raise ValueError("Opponent pool is empty")
        if strategy == "uniform":
            return random.choice(list(self.policies.items()))
        # Weighted or other strategies can be added later
        return random.choice(list(self.policies.items()))
