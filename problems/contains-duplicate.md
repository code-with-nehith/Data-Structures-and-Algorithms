# Contains Duplicate

> Given an array of integers `nums`, return `True` if any value appears **at least twice**, otherwise return `False`.

## 1. **Length Comparison using `set()` (Conceptually simple, operationally inefficient)**

### Idea

Convert the list to a set and compare lengths.

If duplicates exist:

```
len(set(nums)) < len(nums)
```

### Code

```python
def contains_duplicate(nums):
    return len(set(nums)) != len(nums)
```

### Time Complexity

| Case    | Time Complexity | Explanation                                          |
| ------- | --------------- | ---------------------------------------------------- |
| Best    | O(n)            | Entire list must still be traversed to build the set |
| Average | O(n)            | Same reason                                          |
| Worst   | O(n)            | Same reason                                          |

> **Important learning point**:
> Even if the first two elements are duplicates, Python **cannot stop early**.
> The `set()` must process **all elements** before length comparison.

### Space Complexity

| Case | Space |
| ---- | ----- |
| All  | O(n)  |

A new set is created containing all unique elements.

### Pros

* Extremely concise
* Very readable
* Common in interviews for quick correctness

### Cons

* `No early exit`
* Always allocates memory for the full set
* Not suitable when:

  * Input is large
  * Early duplicate detection matters
  * Memory usage must be controlled

## 2. **Using `seen = list()` (Demonstrates linear search cost)**

### Idea

Maintain a list of seen elements.
For each element, check if it already exists in the list.

### Code

```python
def contains_duplicate(nums):
    seen = []
    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False
```

### Time Complexity

| Case    | Time Complexity | Explanation                          |
| ------- | --------------- | ------------------------------------ |
| Best    | O(1)            | Duplicate found in first 2 elements  |
| Average | O(n²)           | Each membership check is O(n)        |
| Worst   | O(n²)           | No duplicates → full scan every time |

> This solution clearly exposes why **linear search inside a loop is expensive**.

### Space Complexity

| Case | Space |
| ---- | ----- |
| All  | O(n)  |

List grows with unique elements.

### Pros

* Very intuitive
* Shows **why data structure choice matters**
* Excellent for beginners to understand performance trade-offs
* Supports **early exit**

### Cons

* Terrible scalability
* Not acceptable for large inputs

## 3. **Using `seen = set()` (Optimal solution)**

### Idea

Replace list with set to achieve O(1) average lookup time.

### Code

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Time Complexity

| Case    | Time Complexity | Explanation                         |
| ------- | --------------- | ----------------------------------- |
| Best    | O(1)            | Duplicate found immediately         |
| Average | O(n)            | Constant-time lookups               |
| Worst   | O(n)            | Hash collisions (rare, theoretical) |

### Space Complexity

| Case | Space |
| ---- | ----- |
| All  | O(n)  |

Set stores unique elements.

### Pros

* Early exit
* Optimal performance
* Scales well
* Industry-standard solution
* Balances time and space efficiently

### Cons

* Slightly more complex than length comparison
* Uses extra memory (unavoidable for fast lookup)

## Comparative Summary

| Approach        | Best Time | Avg Time | Worst Time | Space | Early Exit |
| --------------- | --------- | -------- | ---------- | ----- | ---------- |
| `len(set)`      | O(n)      | O(n)     | O(n)       | O(n)  | ❌          |
| `seen = list()` | O(1)      | O(n²)    | O(n²)      | O(n)  | ✅          |
| `seen = set()`  | O(1)      | O(n)     | O(n)       | O(n)  | ✅          |
