"""
PyCampus Hub
============
A single, all-in-one console application built entirely from Core Python
concepts. Every menu option below is one of the sub-projects, kept as its
own module but wired together here into one program.

Sections (and the Core Python topics each one demonstrates):
  1. Number & String Playground   - variables, data types, expressions, conditionals
  2. Pattern Printing Suite       - loops & iteration, pattern design
  3. To-Do List Manager           - lists, tuples
  4. Student Record System        - dictionaries, sets
  5. Contact Book                 - functions, error/exception handling
  6. Library Management System    - OOP (classes, inheritance, encapsulation)
  7. Bank Account Simulator       - OOP, custom exceptions
  8. Regex Text Validator         - regular expressions
  9. Log File Parser              - regex, dictionaries, error handling
  10. Image Text Extractor (OCR)  - OCR, error handling
  11. Quiz / Exam System          - capstone: combines everything above

Run with:  python main.py
"""

from basics import run_type_playground, run_grade_checker
from patterns import run_pattern_menu
from todo import run_todo_menu
from student_records import run_student_menu
from contacts import run_contacts_menu
from library import run_library_menu
from bank import run_bank_menu
from regex_tools import run_regex_menu
from log_parser import run_log_parser_menu
from ocr_tool import run_ocr_menu
from quiz import run_quiz_menu

MENU = """
==================================================
              PyCampus Hub - Main Menu
==================================================
 1. Number & String Playground
 2. Grade & Eligibility Checker
 3. Pattern Printing Suite
 4. To-Do List Manager
 5. Student Record System
 6. Contact Book
 7. Library Management System
 8. Bank Account Simulator
 9. Regex-based Text Validator
10. Log File Parser
11. Image Text Extractor (OCR)
12. Quiz / Exam System (Capstone)
 0. Exit
==================================================
"""

ROUTES = {
    "1": run_type_playground,
    "2": run_grade_checker,
    "3": run_pattern_menu,
    "4": run_todo_menu,
    "5": run_student_menu,
    "6": run_contacts_menu,
    "7": run_library_menu,
    "8": run_bank_menu,
    "9": run_regex_menu,
    "10": run_log_parser_menu,
    "11": run_ocr_menu,
    "12": run_quiz_menu,
}


def main():
    print("Welcome to PyCampus Hub — one app, every Core Python concept.")
    while True:
        print(MENU)
        choice = input("Select an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = ROUTES.get(choice)
        if action:
            try:
                action()
            except KeyboardInterrupt:
                print("\nCancelled.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid option, please choose a number from the menu.")


if __name__ == "__main__":
    main()
