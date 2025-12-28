# open() - File Operations

## What It Does

Opens files for reading, writing, or appending. Essential for file I/O (input/output) operations.

### File Modes

- **'r'** - Read mode (default) - opens existing file for reading
- **'w'** - Write mode - creates new file or **overwrites** existing file
- **'a'** - Append mode - adds to end of file without deleting content
- **'r+'** - Read and write
- **'w+'** - Write and read (overwrites existing)
- **'a+'** - Append and read

### ⚠️ Important: Always Use Context Manager (with statement)

#### Best Practice ✅

```python
# Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello World\n")
    file.write("My name is Tim")
# File automatically closes when you exit the 'with' block

# Reading from a file
with open("test.txt", "r") as file:
    text = file.read()
    print(text)

# Appending to a file
with open("test.txt", "a") as file:
    file.write("\nNew addition")
```

#### Not Recommended ❌

```python
# Manual open and close
file = open("test.txt", "w")
file.write("Hello World")
file.close()  # Easy to forget! Can cause memory leaks
```

### Why Use 'with'?

1. **Automatic cleanup:** File closes automatically, even if an error occurs
2. **Prevents memory leaks:** Resources are released properly
3. **Cleaner code:** No need to remember to call `.close()`
4. **Error handling:** File closes even if exception is raised

### Write Mode Example

```python
with open("test.txt", "w") as file:
    file.write("Hello World\n")
    file.write("My name is Tim")
```

**Result in test.txt:**
```
Hello World
My name is Tim
```

**⚠️ Warning:** Write mode (`"w"`) completely erases existing file content!

### Read Mode Example

```python
with open("test.txt", "r") as file:
    text = file.read()  # Reads entire file as string
    print(text)
```

### Append Mode Example

```python
with open("test.txt", "a") as file:
    file.write("\nNew addition")
```

Append mode (`"a"`) adds to the end without deleting existing content.

**Before:**
```
Hello World
My name is Tim
```

**After:**
```
Hello World
My name is Tim
New addition
```

### The Newline Character (\n)

When writing to files, `\n` creates a new line:

```python
with open("test.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3")
```

**Result:**
```
Line 1
Line 2
Line 3
```

Without `\n`, everything appears on one line:
```python
with open("test.txt", "w") as file:
    file.write("Line 1")
    file.write("Line 2")
```

**Result:**
```
Line 1Line 2
```

### Context Manager Explanation

The `with` statement creates a "context manager" - a block of code where setup and cleanup happen automatically:

```python
with open("file.txt", "w") as file:
    # Setup: File is opened
    file.write("content")
    # Cleanup: File is automatically closed when we exit this block
```

This is equivalent to:
```python
file = open("file.txt", "w")
try:
    file.write("content")
finally:
    file.close()  # Always runs, even if error occurs
```

But much cleaner!

### Additional File Operations

```python
# Read line by line
with open("test.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes newline characters

# Read all lines into a list
with open("test.txt", "r") as file:
    lines = file.readlines()  # Returns list of lines
    print(lines)

# Read specific number of characters
with open("test.txt", "r") as file:
    first_10_chars = file.read(10)
```