# enumerate() - Get Index and Value Together

## What It Does

Provides both the index (position) and the value when iterating through an iterable. Makes code cleaner and more Pythonic.

### Old Way (Without enumerate)

```python
tasks = ["Write code", "Test code", "Deploy code"]

for index in range(len(tasks)):
    task = tasks[index]
    print(index + 1, task)

# Output:
# 1 Write code
# 2 Test code
# 3 Deploy code
```

### Better Way (With enumerate)

```python
tasks = ["Write code", "Test code", "Deploy code"]

for index, task in enumerate(tasks):
    print(index + 1, task)

# Output:
# 1 Write code
# 2 Test code
# 3 Deploy code
```

### What enumerate Returns

```python
tasks = ["Write code", "Test code", "Deploy code"]

print(list(enumerate(tasks)))
# [(0, 'Write code'), (1, 'Test code'), (2, 'Deploy code')]
```

It returns tuples where:
- First element: index (starting from 0)
- Second element: the actual value

### Starting from Different Index

```python
tasks = ["Write code", "Test code", "Deploy code"]

for index, task in enumerate(tasks, start=1):
    print(index, task)

# Output:
# 1 Write code
# 2 Test code
# 3 Deploy code
```

### Context

- Much cleaner than using `range(len(...))` pattern
- Returns an iterator of tuples: (index, value)
- Useful when you need position information while looping
- Can customize starting index with `start` parameter

**Use Cases:**
- Numbering items in output
- Tracking position while processing data
- Creating indexed lists or menus