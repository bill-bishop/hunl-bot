import torch
import torch.nn.functional as F

def ppo_loss(policy, obs, actions, old_log_probs, returns, advantages, clip_range=0.2, vf_coef=0.5, ent_coef=0.01):
    logits, values, _ = policy(obs)
    probs = torch.softmax(logits, dim=-1)
    dist = torch.distributions.Categorical(probs)

    log_probs = dist.log_prob(actions)
    entropy = dist.entropy().mean()

    ratio = torch.exp(log_probs - old_log_probs)
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1.0 - clip_range, 1.0 + clip_range) * advantages
    policy_loss = -torch.min(surr1, surr2).mean()

    value_loss = F.mse_loss(values.squeeze(-1), returns)

    loss = policy_loss + vf_coef * value_loss - ent_coef * entropy
    return loss, policy_loss.item(), value_loss.item(), entropy.item()
