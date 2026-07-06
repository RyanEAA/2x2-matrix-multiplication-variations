# Strassen-Winograd Permutation Summary

Total permutations checked: **24**

Valid permutations: **[1, 8, 17, 24]**

Number of valid permutations: **4**

---

## Variation 1

Permutation: **1**

### Target \(C'\)

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

### Inferred \(A'\)

```text
[ a, b ]
[ c, d ]
```

### Inferred \(B'\)

```text
[ e, f ]
[ g, h ]
```

### Products

```text
p1 = -(a - c)*(f - h)
p2 = a*e
p3 = b*g
p4 = -(a - c - d)*(e - f + h)
p5 = -(c + d)*(e - f)
p6 = h*(a + b - c - d)
p7 = d*(e - f - g + h)
```

### Reconstruction Matrix

```text
[ p2 + p3, p2 + p4 + p5 + p6 ]
[ p1 + p2 + p4 - p7, p1 + p2 + p4 + p5 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**

---

## Variation 2

Permutation: **8**

### Target \(C'\)

```text
[ a*f + b*h, a*e + b*g ]
[ c*f + d*h, c*e + d*g ]
```

### Inferred \(A'\)

```text
[ a, b ]
[ c, d ]
```

### Inferred \(B'\)

```text
[ f, e ]
[ h, g ]
```

### Products

```text
p1 = -(a - c)*(e - g)
p2 = a*f
p3 = b*h
p4 = (a - c - d)*(e - f - g)
p5 = (c + d)*(e - f)
p6 = g*(a + b - c - d)
p7 = -d*(e - f - g + h)
```

### Reconstruction Matrix

```text
[ p2 + p4 + p5 + p6, p2 + p3 ]
[ p1 + p2 + p4 + p5, p1 + p2 + p4 - p7 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**

---

## Variation 3

Permutation: **17**

### Target \(C'\)

```text
[ c*e + d*g, c*f + d*h ]
[ a*e + b*g, a*f + b*h ]
```

### Inferred \(A'\)

```text
[ c, d ]
[ a, b ]
```

### Inferred \(B'\)

```text
[ e, f ]
[ g, h ]
```

### Products

```text
p1 = (a - c)*(f - h)
p2 = c*e
p3 = d*g
p4 = (a + b - c)*(e - f + h)
p5 = -(a + b)*(e - f)
p6 = -h*(a + b - c - d)
p7 = b*(e - f - g + h)
```

### Reconstruction Matrix

```text
[ p1 + p2 + p4 - p7, p1 + p2 + p4 + p5 ]
[ p2 + p3, p2 + p4 + p5 + p6 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**

---

## Variation 4

Permutation: **24**

### Target \(C'\)

```text
[ c*f + d*h, c*e + d*g ]
[ a*f + b*h, a*e + b*g ]
```

### Inferred \(A'\)

```text
[ c, d ]
[ a, b ]
```

### Inferred \(B'\)

```text
[ f, e ]
[ h, g ]
```

### Products

```text
p1 = (a - c)*(e - g)
p2 = c*f
p3 = d*h
p4 = -(a + b - c)*(e - f - g)
p5 = (a + b)*(e - f)
p6 = -g*(a + b - c - d)
p7 = -b*(e - f - g + h)
```

### Reconstruction Matrix

```text
[ p1 + p2 + p4 + p5, p1 + p2 + p4 - p7 ]
[ p2 + p4 + p5 + p6, p2 + p3 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**
