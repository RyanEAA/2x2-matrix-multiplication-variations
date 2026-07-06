# Matrix Multiplication Variations

This repository explores variations of fast matrix multiplication algorithms through symbolic computation and algebraic reformulation.

The current project investigates equivalent formulations of Strassen's \(2 x 2\) matrix multiplication algorithm.

---

## Motivation

The project began as an attempt to determine whether two \(2 x 2\) matrices could be multiplied using only six scalar multiplications.

Starting from Strassen's seven-multiplication algorithm, I explored permutations of the output matrix, inferred corresponding transformed matrices \(A'\) and \(B'\), and reapplied Strassen's construction to derive equivalent formulations.

---

## Repository Contents

- **Strassen.pdf** — derivations and discussion
- **strassen-variations.py** — symbolic verification using SymPy
- Exhaustive enumeration of all 24 output permutations

---

## Key Results

Using symbolic computation, every permutation of the four output
entries was examined.

For both

- Strassen's algorithm, and
- the Strassen–Winograd variant,

only four of the twenty-four possible output permutations correspond
directly to valid matrix products under the reconstruction method used
in this project.

This suggests that the valid permutations arise from the structure of
the underlying bilinear matrix multiplication map rather than from the
particular 7-multiplication formulation.

---

# Strassen Variations

## Original Strassen

Intermediate products

```text
p1 = a(f-h)
p2 = (a+b)h
p3 = (c+d)e
p4 = d(g-e)
p5 = (a+d)(e+h)
p6 = (b-d)(g+h)
p7 = (a-c)(e+f)
```

Reconstruction

$$
C=
\begin{bmatrix}
p_5+p_4-p_2+p_6 & p_1+p_2\\
p_3+p_4 & p_1+p_5-p_3-p_7
\end{bmatrix}
$$

---

## Variation 1 (Row Swap)

Intermediate products

```text
a1 = c(f-h)
a2 = (c+d)h
a3 = (a+b)e
a4 = b(g-e)
a5 = (c+b)(e+h)
a6 = (d-b)(g+h)
a7 = (c-a)(e+f)
```

Reconstruction

$$
C=
\begin{bmatrix}
a_3+a_4 & a_1+a_5-a_3-a_7\\
a_5+a_4-a_2+a_6 & a_1+a_2
\end{bmatrix}
$$

---

## Variation 2 (Column Swap)

Intermediate products

```text
r1 = a(e-g)
r2 = (a+b)g
r3 = (c+d)f
r4 = d(h-f)
r5 = (a+d)(f+g)
r6 = (b-d)(h+g)
r7 = (a-c)(e+f)
```

Reconstruction

$$
C=
\begin{bmatrix}
r_1+r_2 & r_5+r_4-r_2+r_6\\
r_1+r_5-r_3-r_7 & r_3+r_4
\end{bmatrix}
$$

---

## Variation 3 (Row + Column Swap)

Intermediate products

```text
e1 = c(e-g)
e2 = (c+d)g
e3 = (a+b)f
e4 = b(h-f)
e5 = (c+b)(f+g)
e6 = (d-b)(h+g)
e7 = (c-a)(f+e)
```

Reconstruction

$$
C=
\begin{bmatrix}
e_1+e_5-e_3-e_7 & e_3+e_4\\
e_1+e_2 & e_5+e_4-e_2+e_6
\end{bmatrix}
$$

---

# Strassen–Winograd Variations

The same symbolic permutation search was repeated using the Strassen–Winograd
algorithm. As with the original Strassen formulation, only four output
permutations correspond directly to valid matrix products.

## Original Strassen–Winograd

Intermediate products

```text
w1 = (a-c)(h-f)
w2 = ae
w3 = bg
w4 = (c+d-a)(h-f+e)
w5 = (c+d)(f-e)
w6 = (a+b-c-d)h
w7 = d(e-f-g+h)
```

Reconstruction

$$
C=
\begin{bmatrix}
w_2+w_3 &
w_2+w_4+w_5+w_6 \\
w_1+w_2+w_4-w_7 &
w_1+w_2+w_4+w_5
\end{bmatrix}
$$

---

## Winograd Variation 1

Intermediate products

```text
v1 = (c-a)(h-f)
v2 = ce
v3 = dg
v4 = (a+b-c)(h-f+e)
v5 = (a+b)(f-e)
v6 = -(a+b-c-d)h
v7 = b(e-f-g+h)
```

Reconstruction

$$
C=
\begin{bmatrix}
v_1+v_2+v_4-v_7 &
v_1+v_2+v_4+v_5 \\
v_2+v_3 &
v_2+v_4+v_5+v_6
\end{bmatrix}
$$

---

## Winograd Variation 2

Intermediate products

```text
v1 = (a-c)(g-e)
v2 = af
v3 = bh
v4 = (a-c-d)(e-f-g)
v5 = (c+d)(e-f)
v6 = (a+b-c-d)g
v7 = -d(e-f-g+h)
```

Reconstruction

$$
C=
\begin{bmatrix}
v_2+v_4+v_5+v_6 &
v_2+v_3 \\
v_1+v_2+v_4+v_5 &
v_1+v_2+v_4-v_7
\end{bmatrix}
$$

---

## Winograd Variation 3

Intermediate products

```text
v1 = (a-c)(f-h)
v2 = ce
v3 = dh
v4 = (a+b-c)(e-f+h)
v5 = -(a+b)(e-f)
v6 = -(a+b-c-d)h
v7 = b(e-f-g+h)
```

Reconstruction

$$
C=
\begin{bmatrix}
v_2+v_3 &
v_1+v_2+v_4+v_5 \\
v_1+v_2+v_4-v_7 &
v_2+v_4+v_5+v_6
\end{bmatrix}
$$

---
## Algorithms Implemented

- Strassen's 7-multiplication algorithm
- Strassen–Winograd's 7-multiplication algorithm
---

## Future Work

Future directions include

- investigating additional symmetries of Strassen's algorithm,
- extending the symbolic search to other fast matrix multiplication algorithms,
- exploring whether similar construction techniques apply to larger bilinear algorithms.