# HUNL Bot

Heads-Up No-Limit Poker bot with modular architecture.

## Features
- Environment wrapper around OpenSpiel (with sandbox stubs)
- Abstraction: card bucketing, board textures, bet sizing
- Blueprint training: DeepCFR / NFSP
- RL training: PPO/V-trace, league self-play
- Resolver: subgame re-solving with CFR or NN
- Opponent modeling, league gating
- Evaluation ladders + probes
- Inference: policy runner + server
- CLI tools + training scripts

## Installation

### Sandbox (stubs)
```bash
pip install -r requirements.txt
```
This uses `pyspiel_stub`, `sklearn_stub`, and `torch_stub` for lightweight testing.

### Full setup (dev machine)
```bash
rm -rf third_party/open_spiel
git clone --recursive https://github.com/deepmind/open_spiel.git third_party/open_spiel
cd third_party/open_spiel && mkdir build && cd build
cmake -DPython_EXECUTABLE=$(which python3) ../open_spiel
make -j4
pip install ..
```
Requires Python 3.10+, CMake, g++, protobuf, abseil-cpp, nlohmann/json.

Then install:
```bash
pip install -r requirements.txt
```
(Replace stubs with real `torch` and `scikit-learn`).

## Usage
- Train blueprint: `python -m hunl.cli.train_blueprint --cfg configs/blueprint.deepcfr.yaml`
- Train RL: `python -m hunl.cli.train_rl --cfg configs/rl.ppo.yaml`
- Evaluate: `python -m hunl.cli.eval --cfg configs/eval.yaml`
- Play headless: `python -m hunl.cli.play_headless`

## Repo Layout
See `PROJECT_CHECKLIST.md` for full breakdown of modules, phases, and progress.
