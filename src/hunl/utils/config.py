import yaml
from omegaconf import OmegaConf

class Config:
    @staticmethod
    def load(path):
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return OmegaConf.create(data)
