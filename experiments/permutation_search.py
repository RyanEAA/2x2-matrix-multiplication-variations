from itertools import permutations
import sympy as sp


a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h")

TARGETS = [
    a * e + b * g,
    a * f + b * h,
    c * e + d * g,
    c * f + d * h,
]

TARGET_SET = {sp.expand(x) for x in TARGETS}

ENTRY_INFO = {
    sp.expand(a * e + b * g): {
        "name": "ae+bg",
        "A_row": [a, b],
        "B_col": [e, g],
    },
    sp.expand(a * f + b * h): {
        "name": "af+bh",
        "A_row": [a, b],
        "B_col": [f, h],
    },
    sp.expand(c * e + d * g): {
        "name": "ce+dg",
        "A_row": [c, d],
        "B_col": [e, g],
    },
    sp.expand(c * f + d * h): {
        "name": "cf+dh",
        "A_row": [c, d],
        "B_col": [f, h],
    },
}

def make_symbolic_products(prefix="p"):
    return {
        f"{prefix}{i}": sp.Symbol(f"{prefix}{i}")
        for i in range(1, 8)
    }

def reconstruct_original_C_from_valid_permutation(target_perm, reconstructed_C_prime):
    """
    Given:
      target_perm = the chosen C' entries in row-major order
      reconstructed_C_prime = algorithm reconstruction of A'B' in row-major order

    Return the original C entries ordered as:
      [ae+bg, af+bh, ce+dg, cf+dh]
    """

    mapping = {
        sp.expand(target_perm[i]): sp.expand(reconstructed_C_prime[i])
        for i in range(4)
    }

    return [
        mapping[sp.expand(a*e + b*g)],
        mapping[sp.expand(a*f + b*h)],
        mapping[sp.expand(c*e + d*g)],
        mapping[sp.expand(c*f + d*h)],
    ]

def matrix_product_entries(A, B):
    return [
        sp.expand(A[0][0] * B[0][0] + A[0][1] * B[1][0]),
        sp.expand(A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        sp.expand(A[1][0] * B[0][0] + A[1][1] * B[1][0]),
        sp.expand(A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    ]


def infer_A_B_from_diagonal(target_perm):
    c11 = sp.expand(target_perm[0])
    c22 = sp.expand(target_perm[3])

    row1 = ENTRY_INFO[c11]["A_row"]
    col1 = ENTRY_INFO[c11]["B_col"]

    row2 = ENTRY_INFO[c22]["A_row"]
    col2 = ENTRY_INFO[c22]["B_col"]

    A_prime = [
        row1,
        row2,
    ]

    B_prime = [
        [col1[0], col2[0]],
        [col1[1], col2[1]],
    ]

    return A_prime, B_prime


def run_permutation_search(algorithm_name, algorithm_module, verbose=False):
    results = []

    for idx, target_perm in enumerate(permutations(TARGETS), start=1):
        target_perm = tuple(sp.expand(x) for x in target_perm)

        A_prime, B_prime = infer_A_B_from_diagonal(target_perm)

        product_entries = matrix_product_entries(A_prime, B_prime)
        product_matches_C_prime = product_entries == list(target_perm)

        p_terms = algorithm_module.products(A_prime, B_prime, prefix="p")
        reconstructed = algorithm_module.reconstruct(p_terms, prefix="p")

        symbolic_p_terms = make_symbolic_products(prefix="p")
        symbolic_reconstructed_C_prime = algorithm_module.reconstruct(
            symbolic_p_terms,
            prefix="p",
        )

        reconstruction_valid = reconstructed == product_entries

        if product_matches_C_prime:
            symbolic_reconstruction = reconstruct_original_C_from_valid_permutation(
                target_perm,
                symbolic_reconstructed_C_prime,
            )

            expanded_reconstruction = reconstruct_original_C_from_valid_permutation(
                target_perm,
                reconstructed,
            )

            expanded_reconstruction_valid = expanded_reconstruction == TARGETS
        else:
            symbolic_reconstruction = None
            expanded_reconstruction = None
            expanded_reconstruction_valid = False

        results.append({
            "permutation_number": idx,
            "C_prime": target_perm,
            "A_prime": A_prime,
            "B_prime": B_prime,
            "A_prime_B_prime": product_entries,
            "product_matches_C_prime": product_matches_C_prime,
            "p_terms": p_terms,
            "reconstruction_valid": reconstruction_valid,
            "symbolic_reconstruction": symbolic_reconstruction,
            "expanded_reconstruction": expanded_reconstruction,
            "expanded_reconstruction_valid": expanded_reconstruction_valid,
        })

    print_results(algorithm_name, results)

    return results

def print_results(algorithm_name, results, verbose=False):
    print("\n" + "#" * 80)
    print(f"Algorithm: {algorithm_name}")
    print("#" * 80)

    if verbose:
        for r in results:
            print("=" * 80)
            print(f"Permutation {r['permutation_number']}")

            C1, C2, C3, C4 = r["C_prime"]
            print("C' =")
            print(f"[ {C1}, {C2} ]")
            print(f"[ {C3}, {C4} ]")

            print("\nA' =")
            print(r["A_prime"])

            print("B' =")
            print(r["B_prime"])

            P1, P2, P3, P4 = r["A_prime_B_prime"]
            print("\nA'B' =")
            print(f"[ {P1}, {P2} ]")
            print(f"[ {P3}, {P4} ]")

            print("\np terms:")
            for name, expr in r["p_terms"].items():
                print(f"{name} = {sp.factor(expr)}")

            print(f"\nA'B' equals C'? {r['product_matches_C_prime']}")
            print(
                f"{algorithm_name} reconstruction equals A'B'? "
                f"{r['reconstruction_valid']}"
            )

    valid_count = sum(r["product_matches_C_prime"] for r in results)

    print("\nSummary")
    print(f"Total permutations checked: {len(results)}")
    print(f"Permutations where inferred A'B' equals C': {valid_count}")

    valid_perms = []

    print("\nValid variations")

    for r in results:
        if not r["product_matches_C_prime"]:
            continue

        valid_perms.append(r["permutation_number"])

        print("-" * 80)
        print(f"Variation {len(valid_perms)}")
        print(f"Permutation {r['permutation_number']}")

        print("A' =")
        print(r["A_prime"])

        print("B' =")
        print(r["B_prime"])

        print("\nProducts")
        for name, expr in r["p_terms"].items():
            print(f"{name} = {sp.factor(expr)}")

        F1, F2, F3, F4 = r["symbolic_reconstruction"]

        print("\nReconstruction matrix")
        print(f"[ {F1}, {F2} ]")
        print(f"[ {F3}, {F4} ]")

        E1, E2, E3, E4 = r["expanded_reconstruction"]

        print("\nExpanded result")
        print(f"[ {E1}, {E2} ]")
        print(f"[ {E3}, {E4} ]")
        print(f"Correct? {r['expanded_reconstruction_valid']}")

    print(f"\nValid permutation numbers: {valid_perms}")