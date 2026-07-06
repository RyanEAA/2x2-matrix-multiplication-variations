from algorithms import strassen
from algorithms import winograd
from experiments.permutation_search import run_permutation_search


def main():
    strassen_results = run_permutation_search(
        "Strassen",
        strassen,
    )

    winograd_results = run_permutation_search(
        "Strassen-Winograd",
        winograd,
    )


if __name__ == "__main__":
    main()