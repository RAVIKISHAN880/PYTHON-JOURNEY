# Pyramid Pattern in Python

A simple Python program to print a centered star pyramid using loops and string multiplication.

## Code
```python
row = int(input("ENTER NUMBER OF ROWS :"))
for i in range(1, row + 1):
    print(" " * (row - i), end="")
    print("*" * (2 * i - 1))
```

## Example Output
For `row = 5`:

```text
    *
   ***
  *****
 *******
*********
```

## Concepts Used
- `input()` – Takes the number of rows from the user.
- `for` loop – Iterates through each row.
- String multiplication – Prints spaces and stars.
- `print()` – Displays the pyramid pattern.



