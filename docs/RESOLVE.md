# Re-solving

This document describes how the HUNL bot re-solves subgames during play.

## Boundary Values
- Boundary values are estimated from the blueprint policy.
- Used to cap subgame utilities at re-solve time.

## CFR Re-solver
- Runs a few iterations of Counterfactual Regret Minimization.
- Produces a locally optimal policy conditioned on boundary values.

## NN Re-solver
- Optionally, a trained neural net approximates the re-solving process.

Re-solving allows adaptive play in subgames while staying anchored to the blueprint.
