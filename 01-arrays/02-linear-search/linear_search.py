"""
Linear Search Implementations
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """
    Basic linear search - returns index of target or -1
    
    Args:
        arr: List of elements
        target: Element to search for
    
    Returns:
        int: Index of target or -1 if not found
    
    Examples:
        >>> linear_search([1, 2, 3, 4, 5], 3)
        2
        >>> linear_search([1, 2, 3, 4, 5], 6)
        -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_range(arr, target, start, end):
    """
    Search for target in range [start, end]
    
    Args:
        arr: List of elements
        target: Element to search for
        start: Starting index (inclusive)
        end: Ending index (inclusive)
    
    Returns:
        int: Index of target or -1 if not found
    """
    if start < 0 or end >= len(arr) or start > end:
        return -1
    
    for i in range(start, end + 1):
        if arr[i] == target:
            return i
    return -1


def find_all_occurrences(arr, target):
    """
    Find all indices where target appears
    
    Args:
        arr: List of elements
        target: Element to search for
    
    Returns:
        list: List of indices where target is found
    
    Examples:
        >>> find_all_occurrences([1, 2, 3, 2, 5], 2)
        [1, 3]
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


def find_min(arr):
    """
    Find minimum element using linear search
    
    Args:
        arr: Non-empty list of comparable elements
    
    Returns:
        The minimum element
    
    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    min_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
    return min_val


def find_max(arr):
    """
    Find maximum element using linear search
    
    Args:
        arr: Non-empty list of comparable elements
    
    Returns:
        The maximum element
    
    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val


def count_occurrences(arr, target):
    """
    Count how many times target appears in array
    
    Args:
        arr: List of elements
        target: Element to count
    
    Returns:
        int: Number of occurrences
    """
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count


def search_2d(matrix, target):
    """
    Linear search in 2D array
    
    Args:
        matrix: 2D list (list of lists)
        target: Element to search for
    
    Returns:
        tuple: (row, col) if found, None otherwise
    
    Examples:
        >>> search_2d([[1,2,3],[4,5,6]], 5)
        (1, 1)
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)
    return None


def linear_search_with_condition(arr, condition):
    """
    Search for first element satisfying a condition
    
    Args:
        arr: List of elements
        condition: Function that takes an element and returns bool
    
    Returns:
        int: Index of first element satisfying condition, or -1
    
    Examples:
        >>> linear_search_with_condition([1,2,3,4,5], lambda x: x > 3)
        3
    """
    for i in range(len(arr)):
        if condition(arr[i]):
            return i
    return -1