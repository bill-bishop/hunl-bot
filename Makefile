.PHONY: setup lint test train-blueprint train-rl eval

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

lint:
	flake8 src tests
	black --check src tests
	isort --check-only src tests

fix:
	black src tests
	isort src tests


# Run tests

test:
	pytest -q

# Training commands

train-blueprint:
	python -m hunl.cli.train_blueprint --cfg configs/blueprint.deepcfr.yaml

train-rl:
	python -m hunl.cli.train_rl --cfg configs/rl.ppo.yaml

# Evaluation

eval:
	python -m hunl.cli.eval --cfg configs/eval.yaml
