# Strassen Permutation Summary

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
p1 = e*(c - d)
p2 = d*(e + g)
p3 = a*(f + h)
p4 = -h*(a - b)
p5 = (a + d)*(e + h)
p6 = (b + d)*(g - h)
p7 = (a + c)*(e - f)
```

### Reconstruction Matrix

```text
[ -p2 + p4 + p5 + p6, p3 + p4 ]
[ p1 + p2, p1 - p3 + p5 - p7 ]
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
p1 = f*(c - d)
p2 = d*(f + h)
p3 = a*(e + g)
p4 = -g*(a - b)
p5 = (a + d)*(f + g)
p6 = -(b + d)*(g - h)
p7 = -(a + c)*(e - f)
```

### Reconstruction Matrix

```text
[ p3 + p4, -p2 + p4 + p5 + p6 ]
[ p1 - p3 + p5 - p7, p1 + p2 ]
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
p1 = e*(a - b)
p2 = b*(e + g)
p3 = c*(f + h)
p4 = -h*(c - d)
p5 = (b + c)*(e + h)
p6 = (b + d)*(g - h)
p7 = (a + c)*(e - f)
```

### Reconstruction Matrix

```text
[ p1 + p2, p1 - p3 + p5 - p7 ]
[ -p2 + p4 + p5 + p6, p3 + p4 ]
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
p1 = f*(a - b)
p2 = b*(f + h)
p3 = c*(e + g)
p4 = -g*(c - d)
p5 = (b + c)*(f + g)
p6 = -(b + d)*(g - h)
p7 = -(a + c)*(e - f)
```

### Reconstruction Matrix

```text
[ p1 - p3 + p5 - p7, p1 + p2 ]
[ p3 + p4, -p2 + p4 + p5 + p6 ]
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
