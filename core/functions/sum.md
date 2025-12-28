# sum() - Calculate Total of Numbers

## What It Does

Returns the sum of all numeric values in an iterable.

### Basic Usage

```python
numbers = {1, 2, 3, 4, 10.5, 15}

total = sum(numbers)
print(total)  # 35.5
```

### Advanced: Start Parameter

You can specify a starting value for the sum:

```python
numbers = {1, 2, 3, 4, 10.5, 15}

# Start summing from 10
total = sum(numbers, 10)
print(total)  # 45.5 (35.5 + 10)

# Start from negative value
total = sum(numbers, -10)
print(total)  # 25.5 (35.5 - 10)
```

### Context

- Works with any iterable containing numbers (list, tuple, set)
- All values must be numeric (int or float), otherwise you get an error
- The start parameter defaults to 0 if not specified

**Use Cases:**
- Calculating totals, averages
- Financial calculations
- Statistical operations

```python
# Calculate average
numbers = [10, 20, 30, 40]
average = sum(numbers) / len(numbers)
print(average)  # 25.0