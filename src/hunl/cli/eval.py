import typer
from hunl.eval.ladders import LadderEvaluator
from hunl.utils.config import Config

app = typer.Typer()

@app.command()
def main(cfg: str = "configs/eval.yaml"):
    config = Config.load(cfg)
    agents = {}  # populate with trained policies
    evaluator = LadderEvaluator(agents)
    results = evaluator.run(lambda: None, n_matches=config.eval.matches)
    print("Eval results:", results)

if __name__ == "__main__":
    app()