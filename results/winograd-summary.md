# Strassen-Winograd Permutation Summary

Total cases checked: **48**

Each output permutation is checked in two modes: `AB` and `BA`.

Valid permutation/mode pairs: **[(1, 'AB'), (3, 'BA'), (8, 'AB'), (11, 'BA'), (14, 'BA'), (17, 'AB'), (22, 'BA'), (24, 'AB')]**

Number of valid cases: **8**

---

## Variation 1

Permutation: **1**

Mode: **AB**

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

### Product \(A'B'\)

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
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

Permutation: **3**

Mode: **BA**

### Target \(C'\)

```text
[ a*e + b*g, c*e + d*g ]
[ a*f + b*h, c*f + d*h ]
```

### Inferred \(B'\)

```text
[ e, g ]
[ f, h ]
```

### Inferred \(A'\)

```text
[ a, c ]
[ b, d ]
```

### Product \(B'A'\)

```text
[ a*e + b*g, c*e + d*g ]
[ a*f + b*h, c*f + d*h ]
```

### Products

```text
p1 = -(c - d)*(e - f)
p2 = a*e
p3 = b*g
p4 = -(a - c + d)*(e - f - h)
p5 = -(a - c)*(f + h)
p6 = d*(e - f + g - h)
p7 = h*(a - b - c + d)
```

### Reconstruction Matrix

```text
[ p2 + p3, p1 + p2 + p4 - p7 ]
[ p2 + p4 + p5 + p6, p1 + p2 + p4 + p5 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**

---

## Variation 3

Permutation: **8**

Mode: **AB**

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

### Product \(A'B'\)

```text
[ a*f + b*h, a*e + b*g ]
[ c*f + d*h, c*e + d*g ]
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

## Variation 4

Permutation: **11**

Mode: **BA**

### Target \(C'\)

```text
[ a*f + b*h, c*f + d*h ]
[ a*e + b*g, c*e + d*g ]
```

### Inferred \(B'\)

```text
[ f, h ]
[ e, g ]
```

### Inferred \(A'\)

```text
[ a, c ]
[ b, d ]
```

### Product \(B'A'\)

```text
[ a*f + b*h, c*f + d*h ]
[ a*e + b*g, c*e + d*g ]
```

### Products

```text
p1 = (c - d)*(e - f)
p2 = a*f
p3 = b*h
p4 = (a - c + d)*(e - f + g)
p5 = -(a - c)*(e + g)
p6 = -d*(e - f + g - h)
p7 = g*(a - b - c + d)
```

### Reconstruction Matrix

```text
[ p1 + p2 + p4 - p7, p2 + p3 ]
[ p1 + p2 + p4 + p5, p2 + p4 + p5 + p6 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**

---

## Variation 5

Permutation: **14**

Mode: **BA**

### Target \(C'\)

```text
[ c*e + d*g, a*e + b*g ]
[ c*f + d*h, a*f + b*h ]
```

### Inferred \(B'\)

```text
[ e, g ]
[ f, h ]
```

### Inferred \(A'\)

```text
[ c, a ]
[ d, b ]
```

### Product \(B'A'\)

```text
[ c*e + d*g, a*e + b*g ]
[ c*f + d*h, a*f + b*h ]
```

### Products

```text
p1 = -(a - b)*(e - f)
p2 = c*e
p3 = d*g
p4 = (a - b - c)*(e - f - h)
p5 = (a - c)*(f + h)
p6 = b*(e - f + g - h)
p7 = -h*(a - b - c + d)
```

### Reconstruction Matrix

```text
[ p2 + p4 + p5 + p6, p1 + p2 + p4 + p5 ]
[ p2 + p3, p1 + p2 + p4 - p7 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**

---

## Variation 6

Permutation: **17**

Mode: **AB**

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

### Product \(A'B'\)

```text
[ c*e + d*g, c*f + d*h ]
[ a*e + b*g, a*f + b*h ]
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

## Variation 7

Permutation: **22**

Mode: **BA**

### Target \(C'\)

```text
[ c*f + d*h, a*f + b*h ]
[ c*e + d*g, a*e + b*g ]
```

### Inferred \(B'\)

```text
[ f, h ]
[ e, g ]
```

### Inferred \(A'\)

```text
[ c, a ]
[ d, b ]
```

### Product \(B'A'\)

```text
[ c*f + d*h, a*f + b*h ]
[ c*e + d*g, a*e + b*g ]
```

### Products

```text
p1 = (a - b)*(e - f)
p2 = c*f
p3 = d*h
p4 = -(a - b - c)*(e - f + g)
p5 = (a - c)*(e + g)
p6 = -b*(e - f + g - h)
p7 = -g*(a - b - c + d)
```

### Reconstruction Matrix

```text
[ p1 + p2 + p4 + p5, p2 + p4 + p5 + p6 ]
[ p1 + p2 + p4 - p7, p2 + p3 ]
```

### Expanded Result

```text
[ a*e + b*g, a*f + b*h ]
[ c*e + d*g, c*f + d*h ]
```

Correct: **True**

---

## Variation 8

Permutation: **24**

Mode: **AB**

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

### Product \(A'B'\)

```text
[ c*f + d*h, c*e + d*g ]
[ a*f + b*h, a*e + b*g ]
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
