# range() - Number Sequence Generator

## What It Does

Generates sequences of numbers, primarily used in loops. It's memory-efficient because it doesn't create the entire list upfront.

### Three Ways to Use range()

#### 1. Single Argument (stop only)

```python
range(10)  # Start at 0, stop before 10, step by 1
list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 2. Two Arguments (start, stop)

```python
range(2, 10)  # Start at 2, stop before 10, step by 1
list(range(2, 10))  # [2, 3, 4, 5, 6, 7, 8, 9]
```

#### 3. Three Arguments (start, stop, step)

```python
range(2, 10, 2)  # Start at 2, stop before 10, step by 2
list(range(2, 10, 2))  # [2, 4, 6, 8]
```

### Advanced Usage

#### Counting Backwards

```python
range(10, -10, -2)  # Start at 10, go down to (but not including) -10
list(range(10, -10, -2))  # [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
```

#### In For Loops

```python
for i in range(5):
    print(f"Iteration {i}")
# Prints: Iteration 0, Iteration 1, ... Iteration 4
```

### Important Context

- **Iterator vs List:** `range()` returns a range object (an iterator), not a list
- To see all values at once, convert with `list(range(...))`
- Iterators are memory-efficient - they generate values on-demand rather than storing everything in memory
- The stop value is **exclusive** (not included in the result)

```python
print(range(10))  # Output: range(0, 10) - just shows the range object
print(list(range(10)))  # Output: [0, 1, 2, ..., 9] - shows actual values
```