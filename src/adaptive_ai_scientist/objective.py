def objective(x: float) -> float:
    """Synthetic score to maximize; optimum is x=0.73 with score 1."""
    return 1.0 - (x - 0.73) ** 2
