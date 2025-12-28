# map() - Apply Function to Every Item

## What It Does

Applies a function to every single item in an iterable (list, tuple, set, etc.) and returns the results.

### Syntax

```python
map(function_to_apply, iterable)
```

### Example 1: Built-in Function

```python
strings = ["my", "world", "apple", "pear"]

# Get length of each string
lengths = list(map(len, strings))
print(lengths)  # [2, 5, 5, 4]
```

### Example 2: Lambda Function

Lambda functions are one-line anonymous functions, perfect for simple operations:

```python
strings = ["my", "world", "apple", "pear"]

# Add 's' to each string
result = list(map(lambda x: x + "s", strings))
print(result)  # ['mys', 'worlds', 'apples', 'pears']
```

**Lambda syntax:** `lambda parameter: expression`
- `lambda` is the keyword
- `x` is the parameter (the item being passed)
- `x + "s"` is what gets returned

### Example 3: Custom Function

```python
def add_s(string):
    return string + "s"

strings = ["my", "world", "apple", "pear"]
result = list(map(add_s, strings))
print(result)  # ['mys', 'worlds', 'apples', 'pears']
```

### Context

- **Iterable objects:** Anything you can loop through (lists, tuples, sets, strings, etc.)
- `map()` returns an iterator (map object), so convert with `list()` to see results
- Much cleaner than writing manual loops for simple transformations

**Traditional approach vs map():**
```python
# Without map (manual loop)
strings = ["my", "world", "apple"]
result = []
for s in strings:
    result.append(len(s))

# With map (cleaner)
result = list(map(len, strings))
```