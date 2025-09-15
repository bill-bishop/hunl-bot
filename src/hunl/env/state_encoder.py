import numpy as np

class StateEncoder:
    """
    Encodes hole cards, public cards, and betting state into tensors.
    """

    def __init__(self, num_cards=52):
        self.num_cards = num_cards

    def encode_cards(self, cards):
        """
        One-hot encode cards.
        """
        vec = np.zeros(self.num_cards, dtype=np.float32)
        for c in cards:
            vec[c] = 1.0
        return vec

    def encode_public(self, state):
        return self.encode_cards(state.board_cards())

    def encode_hole(self, state, player):
        return self.encode_cards(state.hole_cards(player))

    def encode_bets(self, state):
        return np.array([state.pot_size(), state.current_player()], dtype=np.float32)

    def encode(self, state, player):
        return np.concatenate([
            self.encode_hole(state, player),
            self.encode_public(state),
            self.encode_bets(state)
        ])
