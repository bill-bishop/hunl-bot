import pyspiel

class SubgameBuilder:
    """
    Constructs public-state subgames from the main game state.
    """
    def __init__(self, game_name="universal_poker"):
        self.game = pyspiel.load_game(game_name)

    def build(self, state):
        if state.is_terminal():
            raise ValueError("Cannot build subgame from terminal state")
        # Clone current state as root of subgame
        subgame_root = state.clone()
        return subgame_root

if __name__ == "__main__":
    game = pyspiel.load_game("universal_poker(betting=betting_nolimit_hunl, numPlayers=2)")
    state = game.new_initial_state()
    builder = SubgameBuilder()
    sub = builder.build(state)
    print("Subgame built at root with history:", sub.history_str())
