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

## Results

The symbolic search examined all

$$
4! = 24
$$

possible permutations of the four entries of the output matrix.

Only **4** permutations correspond directly to valid matrix products under the reconstruction method explored in this project.

These formulations appear to be equivalent to known symmetries of Strassen's algorithm rather than fundamentally new matrix multiplication algorithms.

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

## Future Work

Future directions include

- investigating additional symmetries of Strassen's algorithm,
- extending the symbolic search to other fast matrix multiplication algorithms,
- exploring whether similar construction techniques apply to larger bilinear algorithms.