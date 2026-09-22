"""
Section 4: Student Record System
Covers: Data Structure: Sets, Data Structure: Dictionary
"""


class StudentRecords:
    def __init__(self):
        self.records = {}  # roll_no -> {"name": ..., "subjects": set(...)}

    def add_student(self, roll_no, name, subjects):
        self.records[roll_no] = {"name": name, "subjects": set(subjects)}
        print(f"Added {name} (Roll No {roll_no})")

    def view_student(self, roll_no):
        student = self.records.get(roll_no)
        if not student:
            print("No such student.")
            return
        print(f"{student['name']}: subjects = {sorted(student['subjects'])}")

    def unique_subjects_offered(self):
        all_subjects = set()
        for student in self.records.values():
            all_subjects |= student["subjects"]
        print(f"Unique subjects across all students: {sorted(all_subjects)}")

    def common_subjects(self, roll_a, roll_b):
        a = self.records.get(roll_a)
        b = self.records.get(roll_b)
        if not a or not b:
            print("One or both roll numbers not found.")
            return
        common = a["subjects"] & b["subjects"]
        print(f"Common subjects between {a['name']} and {b['name']}: {sorted(common)}")


def run_student_menu():
    print("\n--- Student Record System ---")
    sr = StudentRecords()
    while True:
        print("\n1. Add student  2. View student  3. Unique subjects  "
              "4. Common subjects  5. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            roll = input("Roll no: ")
            name = input("Name: ")
            subjects = input("Subjects (comma separated): ").split(",")
            sr.add_student(roll, name, [s.strip() for s in subjects if s.strip()])
        elif choice == "2":
            sr.view_student(input("Roll no: "))
        elif choice == "3":
            sr.unique_subjects_offered()
        elif choice == "4":
            a = input("First roll no: ")
            b = input("Second roll no: ")
            sr.common_subjects(a, b)
        elif choice == "5":
            break
        else:
            print("Unknown option.")
