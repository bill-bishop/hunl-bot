import torch
import torch.nn as nn

class ActorCritic(nn.Module):
    def __init__(self, input_dim, hidden_sizes, num_actions, recurrent=False):
        super().__init__()
        layers = []
        last = input_dim
        for h in hidden_sizes:
            layers.append(nn.Linear(last, h))
            layers.append(nn.ReLU())
            last = h
        self.body = nn.Sequential(*layers)

        if recurrent:
            self.rnn = nn.GRU(last, last, batch_first=True)
        else:
            self.rnn = None

        self.policy_head = nn.Linear(last, num_actions)
        self.value_head = nn.Linear(last, 1)

    def forward(self, x, hidden=None):
        z = self.body(x)
        if self.rnn is not None:
            z, hidden = self.rnn(z.unsqueeze(0), hidden)
            z = z.squeeze(0)
        logits = self.policy_head(z)
        value = self.value_head(z)
        return logits, value, hidden
