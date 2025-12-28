# help() - Built-in Documentation

## What It Does

Displays the documentation (docstrings) for any Python object, function, or module without needing to search online.

## Basic Usage

```python
# Get help on built-in functions
help(print)
# Shows complete documentation including parameters

# Get help on methods
help(str.split)

# Get help on modules
help(math)
```

## With Custom Functions

```python
def test_func(a, b):
    """This function adds two numbers.
    
    A docstring is the first string in a function definition.
    It describes what the function does.
    
    Args:
        a (int/float): First number to add
        b (int/float): Second number to add
    
    Returns:
        int/float: Sum of a and b
    """
    return a + b

help(test_func)
# Displays the entire docstring above
```

## Context

- **Docstrings** are documentation strings written inside triple quotes at the start of functions, classes, or modules
- `help()` reads these docstrings and displays them in a formatted way
- This works with built-in functions, libraries, and your own code
- Essential when working with unfamiliar libraries or team codebases

**Use Case:** Quick reference without leaving your code editor or breaking your flow to search documentation online.