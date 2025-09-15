import torch

class RolloutStorage:
    def __init__(self, n_steps, obs_dim, device="cpu"):
        self.obs = torch.zeros((n_steps, obs_dim), dtype=torch.float32, device=device)
        self.actions = torch.zeros((n_steps,), dtype=torch.long, device=device)
        self.log_probs = torch.zeros((n_steps,), dtype=torch.float32, device=device)
        self.rewards = torch.zeros((n_steps,), dtype=torch.float32, device=device)
        self.values = torch.zeros((n_steps,), dtype=torch.float32, device=device)
        self.dones = torch.zeros((n_steps,), dtype=torch.float32, device=device)
        self.ptr = 0
        self.max_steps = n_steps
        self.device = device

    def add(self, obs, action, log_prob, reward, value, done):
        self.obs[self.ptr] = obs
        self.actions[self.ptr] = action
        self.log_probs[self.ptr] = log_prob
        self.rewards[self.ptr] = reward
        self.values[self.ptr] = value
        self.dones[self.ptr] = done
        self.ptr += 1

    def compute_returns_advantages(self, last_value, gamma=0.99, lam=0.95):
        returns = torch.zeros_like(self.rewards, device=self.device)
        advantages = torch.zeros_like(self.rewards, device=self.device)

        gae = 0
        for step in reversed(range(self.max_steps)):
            next_value = last_value if step == self.max_steps - 1 else self.values[step + 1]
            delta = self.rewards[step] + gamma * next_value * (1 - self.dones[step]) - self.values[step]
            gae = delta + gamma * lam * (1 - self.dones[step]) * gae
            advantages[step] = gae
            returns[step] = advantages[step] + self.values[step]

        return returns, advantages

    def get(self):
        return self.obs, self.actions, self.log_probs, self.rewards, self.values, self.dones
