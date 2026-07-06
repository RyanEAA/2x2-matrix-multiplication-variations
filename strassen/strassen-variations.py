from itertools import permutations
import sympy as sp

# Symbols
a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h")

TARGETS = [
    a*e + b*g,  # C11
    a*f + b*h,  # C12
    c*e + d*g,  # C21
    c*f + d*h,  # C22
]

TARGET_SET = {sp.expand(x) for x in TARGETS}

ENTRY_INFO = {
    sp.expand(a*e + b*g): {
        "name": "ae+bg",
        "A_row": [a, b],
        "B_col": [e, g],
    },
    sp.expand(a*f + b*h): {
        "name": "af+bh",
        "A_row": [a, b],
        "B_col": [f, h],
    },
    sp.expand(c*e + d*g): {
        "name": "ce+dg",
        "A_row": [c, d],
        "B_col": [e, g],
    },
    sp.expand(c*f + d*h): {
        "name": "cf+dh",
        "A_row": [c, d],
        "B_col": [f, h],
    },
}


def strassen_products(A, B, prefix="p"):
    x, y = A[0]
    z, w = A[1]

    u, v = B[0]
    s, t = B[1]

    return {
        f"{prefix}1": x * (v - t),
        f"{prefix}2": (x + y) * t,
        f"{prefix}3": (z + w) * u,
        f"{prefix}4": w * (s - u),
        f"{prefix}5": (x + w) * (u + t),
        f"{prefix}6": (y - w) * (s + t),
        f"{prefix}7": (x - z) * (u + v),
    }


def strassen_reconstruct(p):
    p1, p2, p3, p4, p5, p6, p7 = [p[f"p{i}"] for i in range(1, 8)]

    return [
        sp.expand(p5 + p4 - p2 + p6),
        sp.expand(p1 + p2),
        sp.expand(p3 + p4),
        sp.expand(p1 + p5 - p3 - p7),
    ]


def matrix_product_entries(A, B):
    return [
        sp.expand(A[0][0]*B[0][0] + A[0][1]*B[1][0]),
        sp.expand(A[0][0]*B[0][1] + A[0][1]*B[1][1]),
        sp.expand(A[1][0]*B[0][0] + A[1][1]*B[1][0]),
        sp.expand(A[1][0]*B[0][1] + A[1][1]*B[1][1]),
    ]


def infer_A_B_from_diagonal(target_perm):
    """
    Infer A' and B' from C'11 and C'22.

    C'11 gives row 1 of A' and column 1 of B'.
    C'22 gives row 2 of A' and column 2 of B'.
    """
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


def main():
    results = []

    for idx, target_perm in enumerate(permutations(TARGETS), start=1):
        target_perm = tuple(sp.expand(x) for x in target_perm)

        valid_set = set(target_perm) == TARGET_SET

        A_prime, B_prime = infer_A_B_from_diagonal(target_perm)

        product_entries = matrix_product_entries(A_prime, B_prime)
        product_matches_C_prime = product_entries == list(target_perm)

        p = strassen_products(A_prime, B_prime, prefix="p")
        reconstructed = strassen_reconstruct(p)

        reconstruction_valid = reconstructed == product_entries

        results.append({
            "permutation_number": idx,
            "C_prime": target_perm,
            "valid_target_set": valid_set,
            "A_prime": A_prime,
            "B_prime": B_prime,
            "A_prime_B_prime": product_entries,
            "product_matches_C_prime": product_matches_C_prime,
            "p_terms": p,
            "reconstruction_valid": reconstruction_valid,
        })

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
        print(f"Strassen reconstruction equals A'B'? {r['reconstruction_valid']}")

    print("\nSummary")
    print(f"Total permutations checked: {len(results)}")
    print(
        "Permutations where inferred A'B' equals C': "
        f"{sum(r['product_matches_C_prime'] for r in results)}"
    )


if __name__ == "__main__":
    main()