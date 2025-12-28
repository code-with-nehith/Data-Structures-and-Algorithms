# zip() - Combine Multiple Iterables

## What It Does

Combines multiple iterables (lists, tuples, etc.) element-by-element, pairing corresponding items together.

### Old Way (Without zip)

```python
names = ["Alice", "Bob", "Charlie", "Tim"]
ages = [30, 25, 35]

# Need to handle length mismatch manually
for i in range(min(len(names), len(ages))):
    name = names[i]
    age = ages[i]
    print(f"{name} is {age} years old")

# Output:
# Alice is 30 years old
# Bob is 25 years old
# Charlie is 35 years old
```

**Problem:** Lots of manual indexing and need to handle length differences with `min()`.

### Better Way (With zip)

```python
names = ["Alice", "Bob", "Charlie", "Tim"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 30 years old
# Bob is 25 years old
# Charlie is 35 years old
```

Notice "Tim" is excluded because there's no corresponding age.

### Combining Multiple Iterables

```python
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
genders = ["female", "male", "male"]

for name, age, gender in zip(names, ages, genders):
    print(f"{name} is {age} years old and is {gender}")

# Output:
# Alice is 30 years old and is female
# Bob is 25 years old and is male
# Charlie is 35 years old and is male
```

### What zip Returns

```python
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
genders = ["female", "male", "male"]

combined = list(zip(names, ages, genders))
print(combined)
# [('Alice', 30, 'female'), ('Bob', 25, 'male'), ('Charlie', 35, 'male')]
```

Returns tuples pairing corresponding elements from each iterable.

### Context

- **Automatic length handling:** Stops at the shortest iterable
- Returns an iterator of tuples
- Works with any number of iterables
- Much cleaner than manual indexing

**Key Behavior:** If iterables have different lengths, `zip()` stops when the shortest one runs out.

```python
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b']
print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b')]  # Stops at length of list2
```

**Use Cases:**
- Processing parallel data (names with ages, coordinates with labels)
- Combining related information from multiple sources
- Creating dictionaries from separate key and value lists

```python
keys = ["name", "age", "city"]
values = ["Alice", 30, "NYC"]
dictionary = dict(zip(keys, values))
print(dictionary)  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}