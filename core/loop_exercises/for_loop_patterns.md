## 🟢 Level 1 – Very Easy (single loop)

### Q1. Print stars in one line

```
*****
```

👉 Hint: loop 5 times, print `*` without new line.

---

### Q2. Print stars in separate lines

```
*
*
*
*
*
```

👉 Hint: loop 5 times, print `*`.

---

### Q3. Print numbers from 1 to 5

```
1
2
3
4
5
```

👉 Hint: `range(1, 6)`

---

## 🟡 Level 2 – Rectangle patterns (nested loop intro)

### Q4. Print a 3×5 star rectangle

```
*****
*****
*****
```

👉 Hint:

* outer loop = rows
* inner loop = columns

---

### Q5. Print this using numbers

```
1111
2222
3333
```

👉 Hint: print row number multiple times.

---

## 🟠 Level 3 – Right triangle (important 🔥)

### Q6. Print this pattern

```
*
**
***
****
*****
```

👉 Hint:

* outer loop = row (1 to 5)
* inner loop = stars = row number

---

### Q7. Number triangle

```
1
12
123
1234
12345
```

👉 Hint: inner loop runs from `1` to `row`.

---

## 🔵 Level 4 – Reverse patterns

### Q8. Reverse star triangle

```
*****
****
***
**
*
```

👉 Hint:

* outer loop from 5 to 1
* inner loop prints stars

---

### Q9. Reverse numbers

```
12345
1234
123
12
1
```

---

## 🟣 Level 5 – Little thinking (but fun)

### Q10. Same number triangle

```
1
22
333
4444
55555
```

---

### Q11. Continuous numbers

```
1
23
456
78910
```

👉 Hint: use one variable outside loop to store number.


## 🧠 How to think about for-loops (simple rule)

👉 **Outer loop = rows (kitni lines?)**
👉 **Inner loop = columns (har line mein kya print?)**

Example thought:

> “I want 5 rows, and in each row print row number times `*`”
