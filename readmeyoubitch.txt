BBBBB   III  L      L     
B    B   I   L      L     
BBBBB    I   L      L     
B    B   I   L      L     
BBBBB   III  LLLLL  LLLLL 

      IS A STINKER

      _____
    /       \   ♠ A
   |  (•) (•) |  ♣ K
   |    •     |  ♥ Q
    \_______/   ♦ J
      POKER CHIP & CARDS

---

# Heads-Up No-Limit Poker Bot (hunl-bot)

This project is a framework for training and evaluating **Heads-Up No-Limit Texas Hold’em (HUNL)** poker agents. It combines **reinforcement learning (RL)** with **game-theoretic algorithms** to create strong poker-playing strategies.

## Features

- **Abstraction**: Implements card bucketing, bet sizing, and board texture abstractions.
- **Training Algorithms**:
  - Deep Counterfactual Regret Minimization (**DeepCFR**)
  - Neural Fictitious Self-Play (**NFSP**)
  - Policy Gradient / PPO reinforcement learning
- **Environment**: A poker environment that defines the action space, states, and rewards.
- **Resolvers**: Subgame solving using CFR and neural network approximations.
- **League System**: Self-play training with exploiters, gating, and pool management.
- **Evaluation Tools**: Ladder matches, probes, and performance metrics.
- **Inference**: Policy runner and server for deploying trained agents.
- **Utilities**: Logging, configuration, reproducibility, and training orchestration.

## Project Structure

- `configs/` – Configurations for training runs, environments, resolvers, and PPO.
- `src/hunl/` – Core implementation of abstractions, trainers, environments, resolvers, and league play.
- `docs/` & `notebooks/` – Documentation and experiments.
- `docker/` – Containerized execution environment.
- `scripts/` – Training and evaluation scripts (work in progress).
- `{configs,data}/` – Stores checkpoints, rollouts, logs, and card bucket definitions.

## Goal

The purpose of this project is to provide a **research-grade poker AI framework** for studying imperfect-information games, reinforcement learning, and opponent modeling.

---

*This README was auto-generated because the original was empty.*