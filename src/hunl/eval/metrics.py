import numpy as np

class Metrics:
    @staticmethod
    def bb_per_100(rewards, big_blind=100):
        """
        Compute winrate in bb/100 hands.
        """
        total_bb = np.sum(rewards) / big_blind
        hands = len(rewards)
        return (total_bb / hands) * 100

    @staticmethod
    def nash_conv(strategy_values):
        """
        Placeholder for NashConv metric.
        """
        return float(np.mean(np.abs(strategy_values)))
