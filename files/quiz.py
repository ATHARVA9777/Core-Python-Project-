"""
Section 11 (Capstone): Quiz / Exam System
Combines nearly every Core Python topic:
  - OOP (Quiz, Question classes)
  - Dictionaries (question bank) and Lists (option lists)
  - Regex (answer input validation)
  - Custom Exceptions (invalid answer handling)
  - Loops (asking each question)
  - Formatted pattern output (final report card)
"""

import re

ANSWER_RE = re.compile(r"^[A-Da-d]$")


class InvalidAnswerError(Exception):
    pass


class Question:
    def __init__(self, prompt, options, correct):
        self.prompt = prompt
        self.options = options  # list of (label, text) tuples
        self.correct = correct.upper()

    def ask(self):
        print(f"\n{self.prompt}")
        for label, text in self.options:
            print(f"  {label}. {text}")
        while True:
            answer = input("Your answer (A/B/C/D): ").strip()
            if ANSWER_RE.match(answer):
                return answer.upper() == self.correct
            print("Please answer with a single letter A-D.")


class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []  # list of Question objects
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print(f"\n=== {self.title} ===")
        for i, q in enumerate(self.questions, start=1):
            print(f"\n--- Question {i} of {len(self.questions)} ---")
            try:
                correct = q.ask()
            except InvalidAnswerError as e:
                print(f"Skipping question due to error: {e}")
                continue
            if correct:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer was {q.correct}.")
        self.report_card()

    def report_card(self):
        total = len(self.questions)
        pct = (self.score / total * 100) if total else 0
        print("\n" + "*" * 30)
        print("*" + " REPORT CARD ".center(28) + "*")
        print("*" * 30)
        print(f"* Score: {self.score}/{total} ({pct:.1f}%)".ljust(29) + "*")
        verdict = "PASS" if pct >= 40 else "FAIL"
        print(f"* Verdict: {verdict}".ljust(29) + "*")
        print("*" * 30)


def build_default_quiz():
    quiz = Quiz("Core Python Recap Quiz")
    bank = [
        {
            "prompt": "Which data structure is immutable in Python?",
            "options": [("A", "List"), ("B", "Dictionary"), ("C", "Tuple"), ("D", "Set")],
            "correct": "C",
        },
        {
            "prompt": "Which keyword is used to define a function?",
            "options": [("A", "func"), ("B", "def"), ("C", "function"), ("D", "lambda")],
            "correct": "B",
        },
        {
            "prompt": "What does OOP stand for?",
            "options": [
                ("A", "Object Oriented Programming"),
                ("B", "Ordered Output Process"),
                ("C", "Optional Object Pattern"),
                ("D", "Open Operator Protocol"),
            ],
            "correct": "A",
        },
        {
            "prompt": "Which module is used for regular expressions in Python?",
            "options": [("A", "regexp"), ("B", "re"), ("C", "pyregex"), ("D", "match")],
            "correct": "B",
        },
        {
            "prompt": "What does 'except' handle in Python?",
            "options": [
                ("A", "Loops"),
                ("B", "Exceptions"),
                ("C", "Functions"),
                ("D", "Classes"),
            ],
            "correct": "B",
        },
    ]
    for q in bank:
        quiz.add_question(Question(q["prompt"], q["options"], q["correct"]))
    return quiz


def run_quiz_menu():
    quiz = build_default_quiz()
    quiz.run()
