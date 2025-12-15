# Logarithms - The Foundation

Before understanding Big O notation, we need to understand logarithms because they appear frequently in algorithm analysis.

## What is a Logarithm?

A logarithm answers the question: "To what power must we raise a base to get a certain number?"

**Formula**: log₂(8) = 3 means 2³ = 8

In computer science, we usually use log base 2 (written as log₂ or just log).

## Why Logarithms Matter in Algorithms

Logarithms appear when we repeatedly divide something in half. Let me show you:

```python
# Example: How many times can we divide 16 by 2 until we reach 1?
def count_divisions(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
        print(f"After division {count}: n = {n}")
    return count

result = count_divisions(16)
print(f"\nTotal divisions: {result}")
print(f"log₂(16) = {result}")
```

**Output:**
```
After division 1: n = 8
After division 2: n = 4
After division 3: n = 2
After division 4: n = 1

Total divisions: 4
log₂(16) = 4
```

**Key Insight**: If you have 16 items and keep dividing by 2, you need 4 steps to reach 1. This is log₂(16) = 4.

##  The Comparison Table

> This helps visualize the "Growth."

| Input Size (n) | O(1) Steps | O(\log n) Steps | O(n) Steps | O(n^2) Steps |
| --- | --- | --- | --- | --- |
| *8* | 1 | 3 | 8 | 64 |
| *16* | 1 | 4 | 16 | 256 |
| *1,000* | 1 | 10 | 1,000 | 1,000,000 |
| *1,000,000* | 1 | 20 | 1,000,000 | *1 Trillion (Crash!)* |

## How to spot them in Code (The "Cheatsheet")*

* *No Loops?* -> Usually *O(1)*.
* *One Loop?* -> Usually *O(n)*.
* *Loop inside a Loop?* -> Usually *O(n^2)*.
* **Loop that cuts n in half (like i = i / 2)?** -> Usually *O(\log n)*.
## We drop the constants

* O(2n) is just O(n).
* O(500n) is just O(n).
* Why? Because as n goes to infinity, the difference between n and 500n is irrelevant compared to the difference between n and n^2. We only care about the *curve shape*.
