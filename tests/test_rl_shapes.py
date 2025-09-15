def test_network_shapes():
    from hunl.utils import torch  # use stub fallback in sandbox
    from hunl.rl.agents.networks import ActorCritic

    model = ActorCritic(input_dim=10, hidden_sizes=[32], num_actions=4)
    obs = torch.randn(1, 10)
    logits, value, _ = model(obs)
    assert logits.shape[-1] == 4
    assert value.shape[-1] == 1