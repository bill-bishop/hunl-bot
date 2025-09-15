import typer
from hunl.blueprint.deepcfr_trainer import DeepCFRTrainer
from hunl.utils.config import Config

app = typer.Typer()

@app.command()
def main(cfg: str = "configs/blueprint.deepcfr.yaml"):
    config = Config.load(cfg)
    trainer = DeepCFRTrainer(
        game_name=config.game.name,
        hidden_sizes=config.model.hidden_sizes,
        lr=config.train.lr,
        device="cpu"
    )
    trainer.train(num_episodes=config.train.episodes)
    print("Blueprint training complete")

if __name__ == "__main__":
    app()