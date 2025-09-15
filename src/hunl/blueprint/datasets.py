import torch
from torch.utils.data import Dataset

class TrajectoryDataset(Dataset):
    """
    Stores (info_state, action) pairs from CFR/NFSP rollouts.
    """

    def __init__(self, data=None):
        self.data = data or []

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        info, action = self.data[idx]
        return torch.tensor(info, dtype=torch.float32), torch.tensor(action, dtype=torch.long)

    def add(self, info, action):
        self.data.append((info, action))

    def extend(self, batch):
        self.data.extend(batch)
