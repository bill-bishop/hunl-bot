import typer
import pyspiel

app = typer.Typer()

@app.command()
def main():
    print("Starting headless play between agents")
    game = pyspiel.load_game("universal_poker(betting=betting_nolimit_hunl,numPlayers=2)")
    state = game.new_initial_state()
    while not state.is_terminal():
        current_player = state.current_player()
        legal = state.legal_actions()
        action = legal[0]  # naive: always pick first legal action
        state.apply_action(action)
    print("Final returns:", state.returns())

if __name__ == "__main__":
    app()