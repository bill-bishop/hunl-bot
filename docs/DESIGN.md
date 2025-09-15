# HUNL Bot Design Overview

This document describes the system architecture for the Heads-Up No-Limit (HUNL) Poker bot.

## Components
- **Env**: OpenSpiel wrapper with blinds, stack sizes, action masks.
- **Abstraction**: Card bucketing, board textures, bet sizing schemes.
- **Blueprint**: DeepCFR / NFSP training.
- **Resolver**: Subgame re-solving during play.
- **RL**: PPO/IMPALA self-play training.
- **League**: Opponent pools, exploiters, gating for champion selection.
- **Eval**: Metrics, ladder evaluations, probes.
- **Inference**: Policy runner and optional server.

## Flow
1. Train blueprint strategy via DeepCFR.
2. Train reinforcement learning agents with self-play.
3. Build league with exploiters and gated champions.
4. Evaluate via ladder + probes.
5. Export policy for inference.
