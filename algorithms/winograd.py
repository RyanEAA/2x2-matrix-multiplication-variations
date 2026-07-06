import sympy as sp


def products(A, B, prefix="p"):
    x, y = A[0]
    z, w = A[1]

    u, v = B[0]
    s, t = B[1]

    S1 = z + w
    S2 = S1 - x
    S3 = x - z
    S4 = y - S2

    S5 = v - u
    S6 = t - S5
    S7 = t - v
    S8 = S6 - s

    return {
        f"{prefix}1": S3 * S7,
        f"{prefix}2": x * u,
        f"{prefix}3": y * s,
        f"{prefix}4": S2 * S6,
        f"{prefix}5": S1 * S5,
        f"{prefix}6": S4 * t,
        f"{prefix}7": w * S8,
    }


def reconstruct(p, prefix="p"):
    p1, p2, p3, p4, p5, p6, p7 = [
        p[f"{prefix}{i}"] for i in range(1, 8)
    ]

    return [
        sp.expand(p2 + p3),
        sp.expand(p2 + p4 + p5 + p6),
        sp.expand(p1 + p2 + p4 - p7),
        sp.expand(p1 + p2 + p4 + p5),
    ]