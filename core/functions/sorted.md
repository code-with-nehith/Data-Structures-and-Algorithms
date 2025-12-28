# sorted() - Sort Any Iterable

## What It Does

Returns a new sorted list from any iterable. The original iterable remains unchanged.

### Basic Usage

#### Ascending Order (Default)

```python
numbers = [5, 2, 8, 1, 9]
result = sorted(numbers)
print(result)  # [1, 2, 5, 8, 9]
```

#### Descending Order

```python
numbers = [5, 2, 8, 1, 9]
result = sorted(numbers, reverse=True)
print(result)  # [9, 8, 5, 2, 1]
```

### Advanced: key Parameter

The `key` parameter lets you specify a function that determines how to sort items.

#### Sorting Complex Objects

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age (ascending)
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Sort by age (descending)
sorted_people = sorted(people, key=lambda person: person["age"], reverse=True)
print(sorted_people)
# [{'name': 'Charlie', 'age': 35}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
```

**How key works:**
1. The function is applied to each item
2. Items are sorted based on what the function returns
3. In this case, we return `person["age"]`, so sorting happens by age value

#### More Examples

```python
# Sort strings by length
words = ["apple", "pie", "a", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['a', 'pie', 'apple', 'cherry']

# Sort case-insensitive
words = ["banana", "Apple", "cherry", "Date"]
sorted_words = sorted(words, key=str.lower)
print(sorted_words)  # ['Apple', 'banana', 'cherry', 'Date']
```

### Context

- Returns a **new list**, doesn't modify the original
- Works with any iterable (lists, tuples, sets, strings)
- The `key` parameter is powerful for custom sorting logic
- Without `key`, it sorts using default comparison (numbers: numerical, strings: alphabetical)