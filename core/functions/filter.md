# filter() - Keep Only Items That Pass a Test

## What It Does

Filters an iterable by applying a function to each item. If the function returns `True`, the item is kept; if `False`, it's removed.

### Syntax

```python
filter(test_function, iterable)
```

### Example 1: Custom Function

```python
strings = ["my", "world", "apple", "pear"]

def longer_than_four(s):
    return len(s) > 4  # Returns True or False

filtered = list(filter(longer_than_four, strings))
print(filtered)  # ['world', 'apple']
```

**How it works:**
- "my" → len=2 → False → removed
- "world" → len=5 → True → kept
- "apple" → len=5 → True → kept
- "pear" → len=4 → False → removed

### Example 2: Lambda Function

```python
strings = ["my", "world", "apple", "pear"]

filtered = list(filter(lambda x: len(x) > 4, strings))
print(filtered)  # ['world', 'apple']
```

### More Examples

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter numbers greater than 5
greater = list(filter(lambda x: x > 5, numbers))
print(greater)  # [6, 7, 8, 9, 10]
```

### Context

- The filter function must return a boolean (`True` or `False`)
- Returns an iterator, so use `list()` to see results
- Cleaner than writing loops with if statements

**Traditional approach vs filter():**
```python
# Without filter
result = []
for item in strings:
    if len(item) > 4:
        result.append(item)

# With filter
result = list(filter(lambda x: len(x) > 4, strings))
```