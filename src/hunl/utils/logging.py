import logging
from torch.utils.tensorboard import SummaryWriter

class Logger:
    def __init__(self, logdir="runs"):
        self.logger = logging.getLogger("hunl")
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.logger.addHandler(ch)

        self.writer = SummaryWriter(logdir)

    def info(self, msg):
        self.logger.info(msg)

    def log_scalar(self, tag, value, step):
        self.writer.add_scalar(tag, value, step)
