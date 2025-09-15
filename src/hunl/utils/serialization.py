import torch
import os

class Serialization:
    @staticmethod
    def save(model, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        torch.save(model.state_dict(), path)
        print(f"Saved model to {path}")

    @staticmethod
    def load(model, path, map_location="cpu"):
        state = torch.load(path, map_location=map_location)
        model.load_state_dict(state)
        print(f"Loaded model from {path}")
        return model
