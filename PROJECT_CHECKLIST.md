# HUNL Bot Project Checklist

This file tracks implementation progress for the bot. Each phase builds on the previous.

## Phase 1 – Core Environment
- [x] Implement `hunl_env.py` (OpenSpiel wrapper + blinds/stack/reward)
- [x] Implement `action_space.py` (SPR-conditioned bet sizing + masks)
- [x] Implement `state_encoder.py` (encode hole cards, public cards, bets into tensors)
- [x] Implement `reward.py` (final chip deltas, optional baselines)

## Phase 2 – Abstraction
- [x] Implement `card_bucketing.py` (EHS/SDV features, clustering)
- [x] Implement `board_texture.py`
- [x] Implement `bet_sizing_schemes.py`

## Phase 3 – Blueprint
- [x] Implement `deepcfr_trainer.py`
- [x] Implement `nfsp_trainer.py`
- [x] Implement `datasets.py`
- [x] Implement `policy_export.py`

## Phase 4 – RL Training
- [x] Implement `ppo.py`
- [x] Implement `networks.py`
- [x] Implement `actor.py`
- [x] Implement `storage.py`
- [x] Implement `losses.py`
- [x] Implement `distillation.py`

## Phase 5 – Resolver
- [x] Implement `subgame_builder.py`
- [x] Implement `boundaries.py`
- [x] Implement `cfr_resolver.py`
- [x] Implement `nn_resolver.py`

## Phase 6 – League
- [x] Implement `pool.py`
- [x] Implement `exploiters.py`
- [x] Implement `gating.py`

## Phase 7 – Opponent Models
- [x] Implement `stats.py`
- [x] Implement `mix_policy.py`

## Phase 8 – Evaluation
- [x] Implement `ladders.py`
- [x] Implement `metrics.py`
- [x] Implement `probes.py`

## Phase 9 – Utils
- [x] Implement `config.py`
- [x] Implement `seed.py`
- [x] Implement `logging.py`
- [x] Implement `serialization.py`
- [x] Implement `timers.py`

## Phase 10 – Inference
- [x] Implement `policy_runner.py`
- [x] Implement `server.py`

## Phase 11 – CLI + Scripts
- [x] Implement `train_blueprint.py`
- [x] Implement `train_rl.py`
- [x] Implement `eval.py`
- [x] Implement `play_headless.py`
- [x] Fill in shell scripts in `scripts/`

---

### Progress Notes
- Repo scaffold created ✅
- Configs, Makefile, pyproject, pre-commit, gitignore added ✅
- Phase 1 (Env) completed ✅
- Phase 2 (Abstraction) completed ✅
- Phase 3 (Blueprint) completed ✅
- Phase 4 (RL Training) completed ✅
- Phase 5 (Resolver) completed ✅
- Phase 6 (League) completed ✅
- Phase 7 (Opponent Models) completed ✅
- Phase 8 (Evaluation) completed ✅
- Phase 9 (Utils) completed ✅
- Phase 10 (Inference) completed ✅
- Phase 11 (CLI + Scripts) completed ✅
- 🎉 All phases completed