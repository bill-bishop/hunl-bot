import numpy as np

def terminal_reward(state):
    """
    Returns chip deltas at terminal state.
    """
    if not state.is_terminal():
        return np.zeros(state.num_players())
    return np.array(state.returns(), dtype=np.float32)

def normalized_reward(reward, big_blind=100):
    """
    Normalize reward to BB units.
    """
    return reward / big_blind
