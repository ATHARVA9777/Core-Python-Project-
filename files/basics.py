"""
Section 1: Number & String Playground
Covers: Variables, Data Types, Fundamentals of Python Expressions,
        Conditional Statements
"""


def run_type_playground():
    print("\n--- Number & String Playground ---")
    raw = input("Enter something (a number, a word, anything): ").strip()

    # Data type detection / conversion
    if raw.replace('.', '', 1).replace('-', '', 1).isdigit():
        if '.' in raw:
            value = float(raw)
            dtype = "float"
        else:
            value = int(raw)
            dtype = "int"
    else:
        value = raw
        dtype = "str"

    print(f"You entered: {value!r}  -> detected type: {dtype}")

    if dtype in ("int", "float"):
        print(f"Double: {value * 2}")
        print(f"Squared: {value ** 2}")
        # Conditional statements
        if value > 0:
            print("That's a positive number.")
        elif value < 0:
            print("That's a negative number.")
        else:
            print("That's zero.")
    else:
        print(f"Uppercase: {value.upper()}")
        print(f"Reversed: {value[::-1]}")
        print(f"Length: {len(value)}")
        if len(value) > 10:
            print("That's a pretty long string!")
        else:
            print("Nice and short.")


def run_grade_checker():
    """Covers: Conditional Statements"""
    print("\n--- Grade & Eligibility Checker ---")
    try:
        marks = float(input("Enter marks (0-100): "))
    except ValueError:
        print("Please enter a valid number next time.")
        return

    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f"Grade: {grade}")
    print("Result: PASS" if marks >= 40 else "Result: FAIL")
