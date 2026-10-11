import json
from pathlib import Path
from .objective import objective

def run_trials(strategy, n_trials=50, output_path="results/trials.json"):
    history = []
    for step in range(n_trials):
        x = float(strategy.propose(history))
        score = float(objective(x))
        history.append((x, score))
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(
        [{"step": i, "x": x, "score": score} for i, (x, score) in enumerate(history)],
        indent=2
    ) + "\n", encoding="utf-8")
    return history
