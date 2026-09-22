"""
Section 8: Regex-based Text Validator
Covers: Regular Expressions (Regex)
"""

import re

EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$")
PHONE_RE = re.compile(r"^[6-9]\d{9}$")  # simple 10-digit Indian mobile pattern
PAN_RE = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
PASSWORD_RE = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")


def validate_email(text):
    return bool(EMAIL_RE.match(text))


def validate_phone(text):
    return bool(PHONE_RE.match(text))


def validate_pan(text):
    return bool(PAN_RE.match(text.upper()))


def validate_password(text):
    return bool(PASSWORD_RE.match(text))


def extract_emails(paragraph):
    return re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", paragraph)


def extract_numbers(paragraph):
    return re.findall(r"\b\d{10}\b", paragraph)


def run_regex_menu():
    print("\n--- Regex-based Text Validator ---")
    print("1. Validate email\n2. Validate phone\n3. Validate PAN\n"
          "4. Validate password\n5. Extract emails & numbers from a paragraph\n6. Back")
    choice = input("Choose: ").strip()

    if choice == "1":
        text = input("Email: ")
        print("Valid!" if validate_email(text) else "Invalid email format.")
    elif choice == "2":
        text = input("Phone (10 digits): ")
        print("Valid!" if validate_phone(text) else "Invalid phone format.")
    elif choice == "3":
        text = input("PAN: ")
        print("Valid!" if validate_pan(text) else "Invalid PAN format (e.g. ABCDE1234F).")
    elif choice == "4":
        text = input("Password: ")
        print("Strong password!" if validate_password(text)
              else "Weak: needs upper, lower, digit, symbol, 8+ chars.")
    elif choice == "5":
        para = input("Paste a paragraph: ")
        print("Emails found:", extract_emails(para))
        print("10-digit numbers found:", extract_numbers(para))
    elif choice == "6":
        return
    else:
        print("Unknown option.")
