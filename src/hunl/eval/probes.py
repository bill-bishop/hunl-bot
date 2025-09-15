import numpy as np

class ProbeSuite:
    """
    Corner-case probes to stress test policies.
    """
    @staticmethod
    def monotone_board(policy, obs):
        # Probe monotone flush board decisions
        return policy(obs)

    @staticmethod
    def paired_board(policy, obs):
        # Probe paired board spots
        return policy(obs)

    @staticmethod
    def random_probe(policy, obs):
        # Random stress probe
        return policy(obs) + np.random.normal(0, 0.01, size=len(policy(obs)))
