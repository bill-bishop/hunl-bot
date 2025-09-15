# Evaluation

This document describes evaluation methods for the HUNL bot.

## Metrics
- **bb/100**: Winrate measured in big blinds per 100 hands.
- **NashConv**: Distance from equilibrium.

## Ladder Evaluation
- Round-robin evaluation of agents in a league.
- Tracks promotion/demotion of policies.

## Probes
- Corner-case stress tests: monotone boards, paired boards, etc.

Evaluation ensures new policies improve strategically and exploitatively before promotion.
