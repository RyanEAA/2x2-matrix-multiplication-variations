from pathlib import Path
import sympy as sp


def write_results_markdown(algorithm_name, results, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    valid_results = [
        r for r in results
        if r["product_matches_C_prime"]
    ]

    valid_pairs = [
        (r["permutation_number"], r["mode"])
        for r in valid_results
    ]

    lines = []

    lines.append(f"# {algorithm_name} Permutation Summary\n")
    lines.append(f"Total cases checked: **{len(results)}**\n")
    lines.append("Each output permutation is checked in two modes: `AB` and `BA`.\n")
    lines.append(f"Valid permutation/mode pairs: **{valid_pairs}**\n")
    lines.append(f"Number of valid cases: **{len(valid_results)}**\n")

    for i, r in enumerate(valid_results, start=1):
        lines.append("---\n")
        lines.append(f"## Variation {i}\n")
        lines.append(f"Permutation: **{r['permutation_number']}**\n")
        lines.append(f"Mode: **{r['mode']}**\n")

        C1, C2, C3, C4 = r["C_prime"]
        lines.append("### Target \\(C'\\)\n")
        lines.append("```text")
        lines.append(f"[ {C1}, {C2} ]")
        lines.append(f"[ {C3}, {C4} ]")
        lines.append("```\n")

        lines.append(f"### Inferred \\({r['left_label']}\\)\n")
        lines.append("```text")
        lines.append(f"[ {r['left_matrix'][0][0]}, {r['left_matrix'][0][1]} ]")
        lines.append(f"[ {r['left_matrix'][1][0]}, {r['left_matrix'][1][1]} ]")
        lines.append("```\n")

        lines.append(f"### Inferred \\({r['right_label']}\\)\n")
        lines.append("```text")
        lines.append(f"[ {r['right_matrix'][0][0]}, {r['right_matrix'][0][1]} ]")
        lines.append(f"[ {r['right_matrix'][1][0]}, {r['right_matrix'][1][1]} ]")
        lines.append("```\n")

        lines.append(f"### Product \\({r['left_label']}{r['right_label']}\\)\n")
        P1, P2, P3, P4 = r["product_entries"]
        lines.append("```text")
        lines.append(f"[ {P1}, {P2} ]")
        lines.append(f"[ {P3}, {P4} ]")
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