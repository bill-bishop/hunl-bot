# Abstraction

This document describes the abstraction mechanisms used in the HUNL bot.

## Card Bucketing
- Hands are mapped into buckets using EHS (expected hand strength) or SDV (standard deviation).
- Clustering (k-means) groups similar hand strengths.

## Board Texture
- Detects monotone, paired, connected boards.
- Used to refine abstraction for more realistic play.

## Bet Sizing Schemes
- **Coarse**: Small set of representative bet sizes.
- **Rich**: Larger set, allows nuanced strategies.

Abstractions reduce state/action space complexity while maintaining strategic fidelity.
