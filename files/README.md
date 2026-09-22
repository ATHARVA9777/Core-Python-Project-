# PyCampus Hub

A single, menu-driven console application that bundles all your **Core Python**
mini-projects into one program. Each menu option is its own module/section,
so you can study, run, or extend them independently — but they all live under
one roof (`main.py`).

## How to run

```
python main.py
```

## Sections & Core Python topics covered

| # | Section | File | Core Python Topics |
|---|---------|------|---------------------|
| 1 | Number & String Playground | `basics.py` | Variables, Data Types, Expressions |
| 2 | Grade & Eligibility Checker | `basics.py` | Conditional Statements |
| 3 | Pattern Printing Suite | `patterns.py` | Loops & Iterations, Designing Patterns |
| 4 | To-Do List Manager | `todo.py` | Data Structure: List, Tuples |
| 5 | Student Record System | `student_records.py` | Data Structure: Sets, Dictionary |
| 6 | Contact Book | `contacts.py` | Functions, Error/Exception Handling |
| 7 | Library Management System | `library.py` | OOP: Classes, Inheritance, Encapsulation |
| 8 | Bank Account Simulator | `bank.py` | OOP, Custom Exceptions |
| 9 | Regex-based Text Validator | `regex_tools.py` | Regular Expressions |
| 10 | Log File Parser | `log_parser.py` | Regex, Dictionaries, Error Handling |
| 11 | Image Text Extractor (OCR) | `ocr_tool.py` | OCR, Error Handling |
| 12 | Quiz / Exam System (Capstone) | `quiz.py` | Combines nearly all of the above |

## Notes

- `contacts.py` persists contacts to `data/contacts.json` (created automatically).
- `log_parser.py` auto-generates a `data/sample.log` file the first time it runs.
- `ocr_tool.py` needs `pytesseract` + `pillow` (`pip install pytesseract pillow`)
  and the `tesseract-ocr` binary installed on your system. If they're missing,
  it will tell you instead of crashing.
- Every section can also be run standalone by importing its module directly,
  e.g. `from patterns import run_pattern_menu; run_pattern_menu()`.

## Project structure

```
pycampus_hub/
├── main.py              # menu driver — ties every section together
├── basics.py            # sections 1-2
├── patterns.py          # section 3
├── todo.py              # section 4
├── student_records.py   # section 5
├── contacts.py          # section 6
├── library.py           # section 7
├── bank.py              # section 8
├── regex_tools.py       # section 9
├── log_parser.py        # section 10
├── ocr_tool.py          # section 11
├── quiz.py              # section 12 (capstone)
└── data/                # auto-created: contacts.json, sample.log
```
