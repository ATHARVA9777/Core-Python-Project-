"""
Section 2: Pattern Printing Suite
Covers: Loops and Iterations, Designing Patterns
"""


def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)


def diamond(n):
    pyramid(n)
    inverted_pyramid(n - 1)


def number_triangle(n):
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)))


def pascals_triangle(n):
    row = [1]
    for i in range(n):
        print(" ".join(str(x) for x in row).center(n * 4))
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]


def run_pattern_menu():
    print("\n--- Pattern Printing Suite ---")
    print("1. Pyramid\n2. Inverted Pyramid\n3. Diamond\n4. Number Triangle\n5. Pascal's Triangle")
    choice = input("Choose a pattern (1-5): ").strip()
    try:
        n = int(input("Enter size (rows): "))
    except ValueError:
        print("Invalid size, using default of 5.")
        n = 5

    if choice == "1":
        pyramid(n)
    elif choice == "2":
        inverted_pyramid(n)
    elif choice == "3":
        diamond(n)
    elif choice == "4":
        number_triangle(n)
    elif choice == "5":
        pascals_triangle(n)
    else:
        print("Unknown option.")
