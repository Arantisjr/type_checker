# Type Checker Decorator

This repository contains a reusable Python decorator called `type_checker` that enforces type checking on function arguments at runtime using type annotations.

## What is a Decorator?

A **decorator** in Python is a function that wraps another function to add extra features or modify its behavior, without changing the original function's code. Decorators are commonly used for logging, access control, timing, and, as in this case, type checking.

## What Does `type_checker` Do?

The `type_checker` decorator checks if the arguments passed to a function match the types specified in the function's type annotations. If an argument does not match its expected type, a `TypeError` is raised before the function runs.

## How Does It Work?

- Uses the `inspect` module to get information about the function's parameters and their types.
- Binds the actual arguments to the function's signature.
- Checks each argument against its annotated type.
- Raises a `TypeError` if any argument does not match its expected type.

## Usage

1. **Import the decorator:**
    ```python
    from decorator import type_checker
    ```

2. **Add type annotations to your function and decorate it:**
    ```python
    @type_checker
    def greet(name: str, times: int):
        for _ in range(times):
            print(f"Hello, {name}!")
    ```

3. **Call your function:**
    ```python
    greet("Alice", 3)        # Works fine
    greet("Alice", "three")  # Raises TypeError
    ```

## Example

```python
@type_checker
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))      # Output: 5
print(add(2, "3"))    # Raises TypeError: argument b must be <class 'int'>
```

## Notes

- Only arguments with type annotations are checked.
  


