# Diamond Star Pattern in Python

A simple Python program to print a diamond-shaped star pattern using `for` loops and string multiplication.

## Code
```python
row = int(input("Enter number of rows: "))
#upper-half
for i in range(1, row + 1):
    print(" " * (row - i) + "*" * (2 * i - 1))
#lower-half
for i in range(row - 1, 0, -1):
    print(" " * (row - i) + "*" * (2 * i - 1))
```

## Example Output
For `row = 5`:

```text
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

## Concepts Used
- `input()` – Takes the number of rows from the user.
- `for` loops – Print the upper and lower halves.
- String multiplication – Creates spaces and stars.
- `range()` – Controls the pattern's size and direction.



