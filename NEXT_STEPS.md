# Next Steps for HUNL Bot

This guide lists the final setup tasks and how to start training once the environment is ready.

---

## 1. Install Real Dependencies

### Install PyTorch
Pick the right command for your CUDA version (or CPU-only):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Install Scikit-learn
```bash
pip install scikit-learn
```

### Verify
```bash
python -c "import torch, sklearn; print(torch.__version__, sklearn.__version__)"
```

---

## 2. Build and Install OpenSpiel

Clone with submodules:
```bash
rm -rf hunl-bot/third_party/open_spiel
cd hunl-bot/third_party
git clone --recursive https://github.com/deepmind/open_spiel.git
```

Build:
```bash
cd open_spiel
mkdir build && cd build
cmake -DPython_EXECUTABLE=$(which python3) ../open_spiel
make -j$(nproc)
pip install ..
```

Test import:
```bash
python -c "import pyspiel; print(pyspiel.load_game('kuhn_poker'))"
```

---

## 3. Run Tests

From project root:
```bash
cd hunl-bot
PYTHONPATH=src pytest -q
```

All tests should pass using the **real libraries** (no stubs).

---

## 4. Smoke Test CLI

### Train Blueprint
```bash
python -m hunl.cli.train_blueprint --cfg configs/blueprint.deepcfr.yaml
```

### Train RL
```bash
python -m hunl.cli.train_rl --cfg configs/rl.ppo.yaml
```

### Evaluate
```bash
python -m hunl.cli.eval --cfg configs/eval.yaml
```

### Play Headless
```bash
python -m hunl.cli.play_headless
```

---

## 5. Monitor Training

- Check `data/checkpoints/` for saved models.
- Check `data/rollout/` for self-play trajectories.
- Logs in `data/logs/` can be viewed with TensorBoard:
  ```bash
  tensorboard --logdir data/logs
  ```

---

## 6. Validate League & Gating

- Ensure new opponents are added to `league/pool.py`.
- Confirm promotion rules in `league/gating.py` are triggered (CI intervals).

---

## 7. Optional Improvements

- Add CI check to enforce no stub imports.
- Tune hyperparams in `configs/` for larger training runs.
- Switch logging to Weights & Biases (already scaffolded in `utils/logging.py`).

---

## ✅ After completing these steps
You will have a working end-to-end training setup for the HUNL bot with real dependencies and OpenSpiel.