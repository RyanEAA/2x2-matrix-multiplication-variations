# Matrix Multiplication Variations

```md
# Matrix Multiplication Variations

This repository explores symbolic reformulations of fast \(2\times2\) matrix multiplication algorithms.

The current work investigates equivalent formulations of Strassen's and
Strassen–Winograd's 7-multiplication algorithms through symbolic computation.

---

## Motivation

The project began as an attempt to determine whether two \(2\times2\) matrices
could be multiplied using only six scalar multiplications.

Although no 6-multiplication formulation was found, the investigation led to a
symbolic framework for generating and verifying equivalent formulations of
existing bilinear algorithms.

---

## Repository Structure

```

algorithms/
strassen.py
winograd.py

experiments/
permutation_search.py
output.py

results/
strassen-summary.md
winograd-summary.md

paper/
Strassen.pdf

```

---

## Implemented Algorithms

- Strassen (7 multiplications)
- Strassen–Winograd (7 multiplications)

---

## Key Results

Using symbolic computation, all \(4! = 24\) permutations of the output matrix
were examined.

For both implemented algorithms,

- only **4** output permutations correspond to valid matrix products;
- the valid permutations are

```

1, 8, 17, 24

````

These correspond to

- original
- row swap
- column swap
- row + column swap

The symbolic framework automatically

- infers the transformed matrices \(A'\) and \(B'\),
- generates the intermediate products,
- constructs the reconstruction matrix,
- verifies reconstruction of the original product.

---

## Usage

Run

```bash
python run_permutation_search.py
````

to

* enumerate all 24 output permutations,
* verify valid permutations,
* generate

```
results/
    strassen-summary.md
    winograd-summary.md
```

---

## Future Work

Possible future directions include

* additional bilinear matrix multiplication algorithms,
* automatic LaTeX generation,
* automatic paper generation,
* exploration of larger matrix multiplication algorithms.

````

Detailed derivations and generated variations can be found in `results/` and in the accompanying paper.
