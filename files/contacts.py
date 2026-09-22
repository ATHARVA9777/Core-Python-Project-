"""
Section 5: Contact Book
Covers: Functions in Python, Handle Error and Exceptions
"""

import json
import os

CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "data", "contacts.json")


def _load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_contacts(contacts):
    os.makedirs(os.path.dirname(CONTACTS_FILE), exist_ok=True)
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def add_contact(contacts, name, phone):
    contacts[name] = phone
    _save_contacts(contacts)
    print(f"Saved {name}: {phone}")


def search_contact(contacts, name):
    try:
        print(f"{name}: {contacts[name]}")
    except KeyError:
        print(f"No contact named '{name}'.")


def delete_contact(contacts, name):
    try:
        del contacts[name]
        _save_contacts(contacts)
        print(f"Deleted {name}.")
    except KeyError:
        print(f"No contact named '{name}' to delete.")


def update_contact(contacts, name, new_phone):
    if name not in contacts:
        print(f"No contact named '{name}'. Add them first.")
        return
    contacts[name] = new_phone
    _save_contacts(contacts)
    print(f"Updated {name} -> {new_phone}")


def run_contacts_menu():
    print("\n--- Contact Book ---")
    contacts = _load_contacts()
    while True:
        print("\n1. Add  2. Search  3. Update  4. Delete  5. View all  6. Back")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                add_contact(contacts, input("Name: "), input("Phone: "))
            elif choice == "2":
                search_contact(contacts, input("Name: "))
            elif choice == "3":
                update_contact(contacts, input("Name: "), input("New phone: "))
            elif choice == "4":
                delete_contact(contacts, input("Name: "))
            elif choice == "5":
                if contacts:
                    for n, p in contacts.items():
                        print(f"  {n}: {p}")
                else:
                    print("Contact book is empty.")
            elif choice == "6":
                break
            else:
                print("Unknown option.")
        except Exception as e:
            print(f"Something went wrong: {e}")
