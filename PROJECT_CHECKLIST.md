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
- [x] Removed `torch_stub` (now requires real torch) ✅

## Phase 10 – Inference
- [x] Implement `policy_runner.py`
- [x] Implement `server.py`

## Phase 11 – CLI + Scripts
- [x] Implement `train_blueprint.py`
- [x] Implement `train_rl.py`
- [x] Implement `eval.py`
- [x] Implement `play_headless.py` (completed loop ✅)
- [x] Fill in shell scripts in `scripts/`

---

### Progress Notes
- Repo scaffold created ✅
- Configs, Makefile, pyproject, pre-commit, gitignore added ✅
- Phase 1–11 completed ✅
- Stubs removed; now requires **real torch, sklearn, pyspiel** ✅
- Data dirs (`checkpoints`, `rollout`, `logs`) created + gitignored ✅
- TODO in `play_headless.py` resolved ✅

---

### Build Tasks (Sandbox)
- [x] Install core build tools (cmake, g++, make) ✅
- [x] Install zlib, protobuf ✅
- [x] Vendor `nlohmann/json.hpp` ✅
- [ ] Full OpenSpiel build with submodules (`--recursive` clone)
- [ ] Install `torch` and `scikit-learn`

### Test & Validation Tasks
- [ ] Run `pytest -q` with real deps (no stubs)
- [ ] Run smoke tests on CLI commands (`train_blueprint`, `train_rl`, `eval`, `play_headless`) with real deps

### Pre-Training Audit
- [x] Step through configs in `configs/` to ensure hyperparams are realistic ✅
- [x] Step through `src/hunl/` modules to mark any TODOs/incomplete implementations ✅
- [x] Verify data directories (`data/checkpoints`, `data/rollout`, etc.) are git-ignored and auto-created ✅
- [ ] Ensure logging + serialization hooks integrate with training loops
- [ ] Confirm league/gating promotion rules are enforced in code

### Maintenance Tasks
- [x] Sync `requirements.txt` with actual installed packages (`numpy`, `pytest`, typer, etc.) ✅
- [x] Update docs (`README.md`, `docs/`) to reflect sandbox test setup and full OpenSpiel build instructions ✅
- [x] Remove sandbox stubs for torch/sklearn/pyspiel ✅
- [ ] Add automated check in CI to ensure no reintroduction of stub imports