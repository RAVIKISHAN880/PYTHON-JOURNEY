def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=== Basic Calculator ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Quit")

    while True:
        choice = input("\nChoose 1-5: ").strip()

        if choice == "5":
            print("Bye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Try 1-5.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if choice == "1":
            print(f"Result: {a} + {b} = {add(a, b)}")
        elif choice == "2":
            print(f"Result: {a} - {b} = {subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {a} * {b} = {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {a} / {b} = {divide(a, b)}")


if __name__ == "__main__":
    main()
