from algorithms import strassen, winograd
from output import write_results_markdown

from experiments.permutation_search import run_permutation_search

def main():
    strassen_results = run_permutation_search(
        "Strassen",
        strassen,
        verbose=True,
    )

    write_results_markdown(
        "Strassen",
        strassen_results,
        "results/strassen-summary.md",
    )

    winograd_results = run_permutation_search(
        "Strassen-Winograd",
        winograd,
        verbose=False,
    )

    write_results_markdown(
        "Strassen-Winograd",
        winograd_results,
        "results/winograd-summary.md",
    )


if __name__ == "__main__":
    main()