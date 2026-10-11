import random

class RandomStrategy:
    def __init__(self, seed=0):
        self.rng = random.Random(seed)

    def propose(self, history):
        return self.rng.random()

class BestSoFarStrategy:
    """Exploit the best observed point with small local perturbations."""
    def __init__(self, seed=0, radius=0.15):
        self.rng = random.Random(seed)
        self.radius = radius

    def propose(self, history):
        if not history:
            return self.rng.random()
        best_x, _ = max(history, key=lambda row: row[1])
        return min(1.0, max(0.0, best_x + self.rng.uniform(-self.radius, self.radius)))
