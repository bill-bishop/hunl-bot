import typer
from hunl.rl.agents.networks import ActorCritic
from hunl.rl.agents.ppo import PPOAgent
from hunl.rl.rollout.actor import RolloutActor
from hunl.rl.rollout.storage import RolloutStorage
from hunl.utils.config import Config

app = typer.Typer()

@app.command()
def main(cfg: str = "configs/rl.ppo.yaml"):
    config = Config.load(cfg)

    policy = ActorCritic(
        input_dim=config.model.input_dim,
        hidden_sizes=config.model.hidden_sizes,
        num_actions=config.model.num_actions,
    )

    agent = PPOAgent(policy, lr=config.train.lr)
    env_fn = lambda: None  # placeholder, should wrap hunl_env

    for update in range(config.train.updates):
        actor = RolloutActor(env_fn, policy)
        obs, actions, logps, rewards, values, dones = actor.run(n_steps=config.train.n_steps)

        storage = RolloutStorage(config.train.n_steps, config.model.input_dim)
        for i in range(config.train.n_steps):
            storage.add(obs[i], actions[i], logps[i], rewards[i], values[i], dones[i])

        returns, advs = storage.compute_returns_advantages(values[-1])
        rollouts = (obs, actions, logps, returns, advs)
        loss = agent.update(rollouts)
        print(f"Update {update}, loss {loss:.4f}")

if __name__ == "__main__":
    app()