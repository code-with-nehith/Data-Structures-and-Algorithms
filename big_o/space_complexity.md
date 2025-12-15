# Space Complexity - Measuring Memory Usage

Space complexity measures **how much additional memory** an algorithm needs as input grows.

## What Counts as Space?

1. **Input space**: The space taken by input (usually NOT counted)
2. **Auxiliary space**: Extra space used by the algorithm (THIS is what we measure)

## Example 1: Constant Space O(1)

```python
def sum_array_constant_space(arr):
    # Only using one variable regardless of input size
    total = 0  # O(1) space
    
    for num in arr:
        total += num
    
    return total

# No matter if arr has 10 or 10,000 elements,
# we only use one variable 'total'
test = [1, 2, 3, 4, 5]
print(f"Sum: {sum_array_constant_space(test)}")  # Space: O(1)
```

## Example 2: Linear Space O(n)

```python
def create_doubled_array(arr):
    # Creating a new array of the same size
    result = []  # This will grow to size n
    
    for num in arr:
        result.append(num * 2)
    
    return result

test = [1, 2, 3, 4, 5]
doubled = create_doubled_array(test)
print(f"Doubled: {doubled}")  # Space: O(n)
# We created a new list with n elements
```

## Example 3: Space with Recursion

```python
def factorial_recursive(n):
    # Each recursive call adds a frame to the call stack
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# For factorial(5), the call stack looks like:
# factorial(5) → calls factorial(4)
# factorial(4) → calls factorial(3)
# factorial(3) → calls factorial(2)
# factorial(2) → calls factorial(1)
# factorial(1) → returns 1
# 
# Maximum depth: 5 levels
# Space complexity: O(n) due to call stack

print(f"5! = {factorial_recursive(5)}")  # Space: O(n)
```

## Comparing Space: Recursive vs Iterative

```python
# Recursive: O(n) space
def sum_recursive(arr, index=0):
    if index >= len(arr):
        return 0
    return arr[index] + sum_recursive(arr, index + 1)

# Iterative: O(1) space
def sum_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total

test = [1, 2, 3, 4, 5]
print(f"Recursive sum: {sum_recursive(test)}")  # Space: O(n)
print(f"Iterative sum: {sum_iterative(test)}")   # Space: O(1)
```