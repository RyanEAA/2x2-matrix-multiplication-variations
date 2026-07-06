from pathlib import Path
import sympy as sp

def format_matrix(M):
    return f"[ {M[0]}, {M[1]} ]\n[ {M[2]}, {M[3]} ]"


def write_results_markdown(algorithm_name, results, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    valid_results = [
        r for r in results
        if r["product_matches_C_prime"]
    ]

    lines = []

    lines.append(f"# {algorithm_name} Permutation Summary\n")
    lines.append(f"Total permutations checked: **{len(results)}**\n")
    lines.append(f"Valid permutations: **{[r['permutation_number'] for r in valid_results]}**\n")
    lines.append(f"Number of valid permutations: **{len(valid_results)}**\n")

    for i, r in enumerate(valid_results, start=1):
        lines.append("---\n")
        lines.append(f"## Variation {i}\n")
        lines.append(f"Permutation: **{r['permutation_number']}**\n")

        C1, C2, C3, C4 = r["C_prime"]
        lines.append("### Target \\(C'\\)\n")
        lines.append("```text")
        lines.append(f"[ {C1}, {C2} ]")
        lines.append(f"[ {C3}, {C4} ]")
        lines.append("```\n")

        lines.append("### Inferred \\(A'\\)\n")
        lines.append("```text")
        lines.append(f"[ {r['A_prime'][0][0]}, {r['A_prime'][0][1]} ]")
        lines.append(f"[ {r['A_prime'][1][0]}, {r['A_prime'][1][1]} ]")
        lines.append("```\n")

        lines.append("### Inferred \\(B'\\)\n")
        lines.append("```text")
        lines.append(f"[ {r['B_prime'][0][0]}, {r['B_prime'][0][1]} ]")
        lines.append(f"[ {r['B_prime'][1][0]}, {r['B_prime'][1][1]} ]")
        lines.append("```\n")

        lines.append("### Products\n")
        lines.append("```text")
        for name, expr in r["p_terms"].items():
            lines.append(f"{name} = {sp.factor(expr)}")
        lines.append("```\n")

        F1, F2, F3, F4 = r["symbolic_reconstruction"]
        lines.append("### Reconstruction Matrix\n")
        lines.append("```text")
        lines.append(f"[ {F1}, {F2} ]")
        lines.append(f"[ {F3}, {F4} ]")
        lines.append("```\n")

        E1, E2, E3, E4 = r["expanded_reconstruction"]
        lines.append("### Expanded Result\n")
        lines.append("```text")
        lines.append(f"[ {E1}, {E2} ]")
        lines.append(f"[ {E3}, {E4} ]")
        lines.append("```\n")

        lines.append(f"Correct: **{r['expanded_reconstruction_valid']}**\n")

    output_path.write_text("\n".join(lines), encoding="utf-8")