# Linear Search

## Definition

Linear search is a sequential search algorithm that checks every element in the array until the target is found or the array ends.

## Algorithm


1. Start from the first element
2. Compare each element with the target
3. If match found, return index
4. If end reached, return -1 (not found)

## Time Complexity

- **Best Case:** O(1) - Element at first position
- **Average Case:** O(n) - Element at middle
- **Worst Case:** O(n) - Element at end or not present

## Space Complexity

- O(1) - Only uses a few variables

## Pseudocode

```
function linearSearch(array, target):
    for i from 0 to length(array) - 1:
        if array[i] == target:
            return i
    return -1
```

## Variations

1. Search in unsorted array
2. Search in range [start, end]
3. Find first occurrence
4. Find last occurrence
5. Find all occurrences
6. Search with condition
7. Search in 2D array

## Advantages

- Works on unsorted arrays
- Simple to implement
- No preprocessing needed

## Disadvantages

- Slow for large datasets
- O(n) time complexity