# Strassen Permutation Summary

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
p1 = a*(f - h)
p2 = h*(a + b)
p3 = e*(c + d)
p4 = -d*(e - g)
p5 = (a + d)*(e + h)
p6 = (b - d)*(g + h)
p7 = (a - c)*(e + f)
```

### Reconstruction Matrix

```text
[ -p2 + p4 + p5 + p6, p1 + p2 ]
[ p3 + p4, p1 - p3 + p5 - p7 ]
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
p1 = a*(e - g)
p2 = g*(a + b)
p3 = f*(c + d)
p4 = -d*(f - h)
p5 = (a + d)*(f + g)
p6 = (b - d)*(g + h)
p7 = (a - c)*(e + f)
```

### Reconstruction Matrix

```text
[ p1 + p2, -p2 + p4 + p5 + p6 ]
[ p1 - p3 + p5 - p7, p3 + p4 ]
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
p1 = c*(f - h)
p2 = h*(c + d)
p3 = e*(a + b)
p4 = -b*(e - g)
p5 = (b + c)*(e + h)
p6 = -(b - d)*(g + h)
p7 = -(a - c)*(e + f)
```

### Reconstruction Matrix

```text
[ p3 + p4, p1 - p3 + p5 - p7 ]
[ -p2 + p4 + p5 + p6, p1 + p2 ]
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
p1 = c*(e - g)
p2 = g*(c + d)
p3 = f*(a + b)
p4 = -b*(f - h)
p5 = (b + c)*(f + g)
p6 = -(b - d)*(g + h)
p7 = -(a - c)*(e + f)
```

### Reconstruction Matrix

```text
[ p1 - p3 + p5 - p7, p3 + p4 ]
[ p1 + p2, -p2 + p4 + p5 + p6 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**
