import torch

class ActorCritic(torch.nn.Module):
    def __init__(self, input_dim, hidden_sizes, num_actions, recurrent=False):
        super().__init__()
        layers = []
        last = input_dim
        for h in hidden_sizes:
            layers.append(torch.nn.Linear(last, h))
            layers.append(lambda x: x)  # stub ReLU as identity
            last = h
        self.body = layers

        self.rnn = None  # stub ignores recurrent for now
        self.policy_head = torch.nn.Linear(last, num_actions)
        self.value_head = torch.nn.Linear(last, 1)

    def forward(self, x, hidden=None):
        z = x
        for layer in self.body:
            z = layer(z)
        logits = self.policy_head(z)
        value = self.value_head(z)
        return logits, value, hidden