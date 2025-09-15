def test_metrics():
    from hunl.eval.metrics import Metrics
    rewards = [100, -50, 25]
    bb100 = Metrics.bb_per_100(rewards, big_blind=50)
    assert isinstance(bb100, float)
    nc = Metrics.nash_conv([0.1, -0.2, 0.05])
    assert isinstance(nc, float)