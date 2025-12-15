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