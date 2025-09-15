import numpy as np
from . import pyspiel  # use real pyspiel or stub fallback

class HunlEnv:
    """
    Heads-Up No-Limit Hold'em environment wrapper using OpenSpiel.
    Provides reset(), step(), and observation encoding.
    """

    def __init__(self, blinds=(50, 100), stack=20000, rake=0.0, antes=0):
        self.blinds = blinds
        self.stack = stack
        self.rake = rake
        self.antes = antes

        game_string = (
            f"universal_poker(betting=betting_nolimit_hunl," \
            f"numPlayers=2,stack={stack},blinds={blinds[0]},{blinds[1]}," \
            f"antes={antes},rake={rake})"
        )
        self.game = pyspiel.load_game(game_string)
        self.reset()

    def reset(self):
        self.state = self.game.new_initial_state()
        return self._get_obs()

    def step(self, action):
        """
        Apply action to the environment.
        Returns (obs, reward, done, info)
        """
        self.state.apply_action(action)
        done = self.state.is_terminal()
        reward = np.array(self.state.returns()) if done else np.zeros(2)
        return self._get_obs(), reward, done, {}

    def legal_actions(self):
        return self.state.legal_actions()

    def current_player(self):
        return self.state.current_player()

    def _get_obs(self):
        return self.state.information_state_tensor(self.state.current_player())


if __name__ == "__main__":
    env = HunlEnv()
    obs = env.reset()
    print("Initial obs shape:", len(obs))
    for a in env.legal_actions():
        print("Legal action:", a)