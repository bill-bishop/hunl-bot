import torch
import torch.nn as nn
import torch.optim as optim
from hunl.rl.losses import ppo_loss

class PPOAgent:
    def __init__(self, policy, lr=3e-4, clip_range=0.2, vf_coef=0.5, ent_coef=0.01, device="cpu"):
        self.policy = policy.to(device)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)
        self.clip_range = clip_range
        self.vf_coef = vf_coef
        self.ent_coef = ent_coef
        self.device = device

    def update(self, rollouts, epochs=4, batch_size=64):
        obs, actions, old_log_probs, returns, advantages = rollouts

        dataset = torch.utils.data.TensorDataset(obs, actions, old_log_probs, returns, advantages)
        loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

        for _ in range(epochs):
            for batch in loader:
                obs_b, act_b, old_logp_b, ret_b, adv_b = [x.to(self.device) for x in batch]
                loss, policy_loss, value_loss, entropy = ppo_loss(
                    self.policy, obs_b, act_b, old_logp_b, ret_b, adv_b,
                    clip_range=self.clip_range, vf_coef=self.vf_coef, ent_coef=self.ent_coef
                )
                self.optimizer.zero_grad()
                loss.backward()
                nn.utils.clip_grad_norm_(self.policy.parameters(), 0.5)
                self.optimizer.step()

        return loss.item()
