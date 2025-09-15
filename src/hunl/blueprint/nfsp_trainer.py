import torch
import torch.nn as nn
import torch.optim as optim
import random
import pyspiel

class NFSPPolicy(nn.Module):
    def __init__(self, input_dim, hidden_sizes, num_actions):
        super().__init__()
        layers = []
        last = input_dim
        for h in hidden_sizes:
            layers.append(nn.Linear(last, h))
            layers.append(nn.ReLU())
            last = h
        layers.append(nn.Linear(last, num_actions))
        layers.append(nn.Softmax(dim=-1))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)


class NFSPTrainer:
    def __init__(self, game_name="universal_poker", hidden_sizes=[128, 128], lr=1e-3, device="cpu"):
        self.game = pyspiel.load_game(game_name)
        self.info_state_size = self.game.information_state_tensor_size()
        self.num_actions = self.game.num_distinct_actions()

        self.policy_net = NFSPPolicy(self.info_state_size, hidden_sizes, self.num_actions).to(device)
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=lr)
        self.device = device

    def sample_episode(self, state, trajectory):
        if state.is_terminal():
            return state.returns()
        elif state.is_chance_node():
            outcomes = state.chance_outcomes()
            a, _ = random.choice(outcomes)
            state.apply_action(a)
            return self.sample_episode(state, trajectory)
        else:
            player = state.current_player()
            info_tensor = torch.tensor(state.information_state_tensor(player), dtype=torch.float32).to(self.device)
            legal = state.legal_actions()

            probs = self.policy_net(info_tensor)
            action = random.choice(legal)
            state.apply_action(action)

            trajectory.append((player, info_tensor.detach(), action))
            return self.sample_episode(state, trajectory)

    def train_step(self, trajectory):
        for player, info, action in trajectory:
            info = info.unsqueeze(0)
            probs = self.policy_net(info)
            target = torch.zeros_like(probs)
            target[0, action] = 1.0

            loss = -torch.sum(target * torch.log(probs + 1e-8))
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

    def train(self, num_episodes=100):
        for _ in range(num_episodes):
            state = self.game.new_initial_state()
            traj = []
            self.sample_episode(state, traj)
            self.train_step(traj)


if __name__ == "__main__":
    trainer = NFSPTrainer()
    trainer.train(num_episodes=10)
    print("NFSP training run complete")
