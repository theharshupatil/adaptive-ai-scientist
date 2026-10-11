# Adaptive AI Scientist

A small experimental framework for selecting experiments, evaluating outcomes, and choosing the next experiment. The initial version uses a synthetic objective so the full loop can run without an LLM or expensive compute.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
python -m adaptive_ai_scientist.demo
```

## First milestone

The demo compares a random-search baseline with a simple best-so-far strategy over a synthetic objective. This is infrastructure for experiments, not an autonomous scientific discovery system.

## Layout

- `objective.py`: synthetic objective with a known optimum.
- `runner.py`: run and record trials.
- `strategies.py`: random and best-so-far proposal strategies.
- `demo.py`: end-to-end demonstration.

## Next milestones

- [ ] Add seeded baselines and multiple independent trials.
- [ ] Compare random search, grid search, and Bayesian optimization.
- [ ] Add experiment budgets and cost-aware objective functions.
- [ ] Support pluggable model-training or simulation objectives.
- [ ] Add uncertainty estimates and report regret versus budget.

The framework should make experiments reproducible: log configuration, seed, metric, elapsed time, and software version.
