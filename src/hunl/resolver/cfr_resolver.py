import random

class CFRResolver:
    """
    Few-iteration CFR subgame re-solver.
    """
    def __init__(self, iterations=100):
        self.iterations = iterations

    def resolve(self, subgame_root):
        """
        Run CFR iterations from subgame root.
        """
        strategy = {}
        for _ in range(self.iterations):
            self._cfr(subgame_root, 1.0, 1.0, strategy)
        return strategy

    def _cfr(self, state, pi1, pi2, strategy):
        if state.is_terminal():
            returns = state.returns()
            return returns[state.current_player()]
        if state.is_chance_node():
            v = 0.0
            for a, p in state.chance_outcomes():
                child = state.clone()
                child.apply_action(a)
                v += p * self._cfr(child, pi1, pi2, strategy)
            return v

        player = state.current_player()
        legal = state.legal_actions()
        if not legal:
            return 0.0

        strategy[player] = [1.0 / len(legal)] * len(legal)
        values = []
        for a in legal:
            child = state.clone()
            child.apply_action(a)
            values.append(self._cfr(child, pi1, pi2, strategy))

        return sum(values) / len(values)
