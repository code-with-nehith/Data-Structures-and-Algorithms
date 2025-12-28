# print() - Output with Control

## What It Does

Displays output to the console/terminal. It's typically the first function beginners learn, but it has advanced features most people don't know about.

## Basic Usage

```python
name = "Alice"
age = 23
print("My name is", name, "and I am", age, "years old")
# Output: My name is Alice and I am 23 years old
```

## Advanced Parameters

### **sep** Parameter - Custom Separators

By default, `print()` separates multiple arguments with a space. You can change this:

```python
# Default behavior (space separator)
print("My", "name", "is", "Alice")
# Output: My name is Alice

# Custom separator with pipe
print("My", "name", "is", name, "and", "I", "am", age, "years old", sep="|")
# Output: My|name|is|Alice|and|I|am|23|years old

# Comma separator (useful for CSV-like output)
print("My", "name", "is", "Alice", sep=", ")
# Output: My, name, is, Alice
```

**Use Case:** Formatting output for files, logs, or specific display requirements without manual string concatenation.

### **end** Parameter - Control Line Endings

By default, `print()` adds a newline character (`\n`) at the end, moving to the next line. You can override this:

```python
# Default behavior (moves to next line)
print("Hello")
print("World")
# Output:
# Hello
# World

# Custom ending (stays on same line)
print("Hello", end=" | ")
print("World")
# Output: Hello | World

# No ending at all
print("Loading", end="")
print("...")
# Output: Loading...
```

**Use Case:** Progress indicators, inline status updates, or creating custom formatted output.

## Context

The `\n` (backslash n) is the newline character - it tells the terminal to move to the next line. When you override `end`, you're changing what gets printed after your content.