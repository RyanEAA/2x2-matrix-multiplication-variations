import sympy as sp


def products(A, B, prefix="p"):
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


def reconstruct(p, prefix="p"):
    p1, p2, p3, p4, p5, p6, p7 = [
        p[f"{prefix}{i}"] for i in range(1, 8)
    ]

    return [
        sp.expand(p5 + p4 - p2 + p6),
        sp.expand(p1 + p2),
        sp.expand(p3 + p4),
        sp.expand(p1 + p5 - p3 - p7),
    ]