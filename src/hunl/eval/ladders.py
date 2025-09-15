import random
import numpy as np

class LadderEvaluator:
    """
    Runs round-robin ladder evaluation among agents.
    """
    def __init__(self, agents):
        self.agents = agents

    def run(self, env_fn, n_matches=100):
        results = {a: {b: [] for b in self.agents} for a in self.agents}
        for a in self.agents:
            for b in self.agents:
                if a == b:
                    continue
                for _ in range(n_matches):
                    env = env_fn()
                    state = env.reset()
                    done = False
                    while not done:
                        player = env.current_player()
                        if player == 0:
                            action = self.agents[a].act(state)
                        else:
                            action = self.agents[b].act(state)
                        state, reward, done, _ = env.step(action)
                    results[a][b].append(reward[0])
        return results
