import torch

class PolicyRunner:
    """
    Loads a trained policy and runs inference.
    """
    def __init__(self, model, checkpoint_path, device="cpu"):
        self.model = model.to(device)
        self.device = device
        self.model.load_state_dict(torch.load(checkpoint_path, map_location=device))
        self.model.eval()

    def act(self, obs):
        obs_t = torch.tensor(obs, dtype=torch.float32).to(self.device)
        with torch.no_grad():
            logits, value, _ = self.model(obs_t)
            probs = torch.softmax(logits, dim=-1).cpu().numpy()
        return probs
