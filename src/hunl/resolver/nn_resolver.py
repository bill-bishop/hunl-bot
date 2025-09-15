import torch
import torch.nn as nn

class NNResolver(nn.Module):
    """
    Learned neural network-based resolver.
    """
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

    def resolve(self, state):
        obs = torch.tensor(state.information_state_tensor(state.current_player()), dtype=torch.float32)
        with torch.no_grad():
            return self.forward(obs)
