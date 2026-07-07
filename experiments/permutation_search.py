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

ENTRY_INFO_AB = {
    sp.expand(a * e + b * g): {"left_row": [a, b], "right_col": [e, g]},
    sp.expand(a * f + b * h): {"left_row": [a, b], "right_col": [f, h]},
    sp.expand(c * e + d * g): {"left_row": [c, d], "right_col": [e, g]},
    sp.expand(c * f + d * h): {"left_row": [c, d], "right_col": [f, h]},
}

ENTRY_INFO_BA = {
    sp.expand(a * e + b * g): {"left_row": [e, g], "right_col": [a, b]},
    sp.expand(a * f + b * h): {"left_row": [f, h], "right_col": [a, b]},
    sp.expand(c * e + d * g): {"left_row": [e, g], "right_col": [c, d]},
    sp.expand(c * f + d * h): {"left_row": [f, h], "right_col": [c, d]},
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


def infer_left_right_from_diagonal(target_perm, entry_info):
    c11 = sp.expand(target_perm[0])
    c22 = sp.expand(target_perm[3])

    row1 = entry_info[c11]["left_row"]
    col1 = entry_info[c11]["right_col"]

    row2 = entry_info[c22]["left_row"]
    col2 = entry_info[c22]["right_col"]

    left_matrix = [
        row1,
        row2,
    ]

    right_matrix = [
        [col1[0], col2[0]],
        [col1[1], col2[1]],
    ]

    return left_matrix, right_matrix


def run_permutation_search(algorithm_name, algorithm_module, verbose=False):
    results = []
    for idx, target_perm in enumerate(permutations(TARGETS), start=1):
        target_perm = tuple(sp.expand(x) for x in target_perm)

        inference_modes = [
            ("AB", "A'", "B'", ENTRY_INFO_AB),
            ("BA", "B'", "A'", ENTRY_INFO_BA),
        ]

        for mode_name, left_label, right_label, entry_info in inference_modes:
            left_matrix, right_matrix = infer_left_right_from_diagonal(
                target_perm,
                entry_info,
            )

            product_entries = matrix_product_entries(left_matrix, right_matrix)
            product_matches_C_prime = product_entries == list(target_perm)

            p_terms = algorithm_module.products(left_matrix, right_matrix, prefix="p")
            reconstructed = algorithm_module.reconstruct(p_terms, prefix="p")

            reconstruction_valid = reconstructed == product_entries

            symbolic_p_terms = make_symbolic_products(prefix="p")
            symbolic_reconstructed_C_prime = algorithm_module.reconstruct(
                symbolic_p_terms,
                prefix="p",
            )

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
                "mode": mode_name,
                "left_label": left_label,
                "right_label": right_label,
                "C_prime": target_perm,
                "left_matrix": left_matrix,
                "right_matrix": right_matrix,
                "product_entries": product_entries,
                "product_matches_C_prime": product_matches_C_prime,
                "p_terms": p_terms,
                "reconstruction_valid": reconstruction_valid,
                "symbolic_reconstruction": symbolic_reconstruction,
                "expanded_reconstruction": expanded_reconstruction,
                "expanded_reconstruction_valid": expanded_reconstruction_valid,
            })

    print_results(algorithm_name, results, verbose=verbose)

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

            print(f"\nMode: {r['mode']}")

            print(f"{r['left_label']} =")
            print(r["left_matrix"])

            print(f"{r['right_label']} =")
            print(r["right_matrix"])

            P1, P2, P3, P4 = r["product_entries"]
            print(f"\n{r['left_label']}{r['right_label']} =")
            print(f"[ {P1}, {P2} ]")
            print(f"[ {P3}, {P4} ]")

            print("\np terms:")
            for name, expr in r["p_terms"].items():
                print(f"{name} = {sp.factor(expr)}")

            print(f"\n{r['left_label']}{r['right_label']} equals C'? {r['product_matches_C_prime']}")
            print(
                f"{algorithm_name} reconstruction equals {r['left_label']}{r['right_label']}? "
                f"{r['reconstruction_valid']}"
            )

    valid_count = sum(r["product_matches_C_prime"] for r in results)

    print("\nSummary")
    print(f"Total permutations checked: {len(results)}")
    print(f"Valid inference/mode pairs where product equals C': {valid_count}")
    valid_perms = []

    print("\nValid variations")

    for r in results:
        if not r["product_matches_C_prime"]:
            continue

        valid_perms.append((r["permutation_number"], r["mode"]))

        print("-" * 80)
        print(f"Variation {len(valid_perms)}")
        print(f"Permutation {r['permutation_number']}")
        print(f"Mode: {r['mode']}")

        print(f"{r['left_label']} =")
        print(r["left_matrix"])

        print(f"{r['right_label']} =")
        print(r["right_matrix"])

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