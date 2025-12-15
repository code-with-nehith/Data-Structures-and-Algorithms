# Time Complexity - Measuring Algorithm Speed

Time complexity measures **how the runtime grows** as the input size increases.

> **Important:** We Don't Measure Actual Time

We don't say "this takes 5 seconds." Instead, we say "this takes n steps" or "n² steps" where n is the input size.

## Example 1

```python
def counting_operations(n):
    # Operation 1: Simple assignment (1 operation)
    total = 0
    
    # Operation 2: Loop runs n times
    for i in range(n):
        total += i  # This happens n times
    
    # Operation 3: Another simple operation (1 operation)
    return total

# If n = 5, we have: 1 + 5 + 1 = 7 operations
# If n = 100, we have: 1 + 100 + 1 = 102 operations
# The dominant factor is n, so time complexity is O(n)
```

## Example 2

```python
def get_max(arr):
    n = len(arr)
    
    # Line 1: 1 operation
    max_val = arr[0]
    
    # Line 2: This loop runs n-1 times
    for i in range(1, n):
        # Line 3: 1 comparison (runs n-1 times)
        if arr[i] > max_val:
            # Line 4: 1 assignment (runs at most n-1 times)
            max_val = arr[i]
    
    # Line 5: 1 operation
    return max_val

# Total operations: 1 + (n-1) + (n-1) + 1 = 2n
# We ignore constants, so this is O(n)

test_array = [3, 7, 2, 9, 1, 5]
print(f"Maximum value: {detailed_counting(test_array)}")
```