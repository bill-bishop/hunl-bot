import torch
import numpy as np

class RolloutActor:
    def __init__(self, env_fn, policy, device="cpu"):
        self.env = env_fn()
        self.policy = policy
        self.device = device

    def run(self, n_steps=128):
        obs_buf, act_buf, logp_buf, rew_buf, val_buf, done_buf = [], [], [], [], [], []

        obs = self.env.reset()
        for _ in range(n_steps):
            obs_t = torch.tensor(obs, dtype=torch.float32).to(self.device)
            logits, value, _ = self.policy(obs_t)
            probs = torch.softmax(logits, dim=-1)
            dist = torch.distributions.Categorical(probs)
            action = dist.sample()

            next_obs, reward, done, _ = self.env.step(action.item())

            obs_buf.append(obs_t.cpu())
            act_buf.append(action.cpu())
            logp_buf.append(dist.log_prob(action).detach().cpu())
            rew_buf.append(torch.tensor(reward, dtype=torch.float32))
            val_buf.append(value.detach().cpu())
            done_buf.append(torch.tensor(done, dtype=torch.float32))

            obs = next_obs if not done else self.env.reset()

        return (
            torch.stack(obs_buf),
            torch.stack(act_buf),
            torch.stack(logp_buf),
            torch.stack(rew_buf),
            torch.stack(val_buf),
            torch.stack(done_buf)
        )
