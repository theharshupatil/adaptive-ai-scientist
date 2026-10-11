import json
from adaptive_ai_scientist.runner import run_trials
from adaptive_ai_scientist.strategies import RandomStrategy

def test_runner_records_trials(tmp_path):
    output = tmp_path / "trials.json"
    results = run_trials(RandomStrategy(seed=1), n_trials=5, output_path=output)
    data = json.loads(output.read_text())
    assert len(results) == 5
    assert len(data) == 5
    assert all(0.0 <= row["x"] <= 1.0 for row in data)
