from .runner import run_trials
from .strategies import BestSoFarStrategy, RandomStrategy

def main():
    random_results = run_trials(RandomStrategy(seed=3), output_path="results/random.json")
    adaptive_results = run_trials(BestSoFarStrategy(seed=3), output_path="results/best_so_far.json")
    print(f"random best score: {max(score for _, score in random_results):.4f}")
    print(f"best-so-far best score: {max(score for _, score in adaptive_results):.4f}")
    print("Results written to results/")

if __name__ == "__main__":
    main()
