"""
Section 7: Bank Account Simulator
Covers: OOP Principles (inheritance), Handle Error and Exceptions (custom exceptions)
"""


class InsufficientFundsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # encapsulated

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}; balance is only {self._balance}."
            )
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self._balance}")

    @property
    def balance(self):
        return self._balance


class SavingsAccount(Account):
    """Inherits from Account; adds interest calculation."""

    def __init__(self, owner, balance=0, interest_rate=0.04):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Applied {self.interest_rate * 100:.1f}% interest: +{interest:.2f}. "
              f"New balance: {self._balance:.2f}")


def run_bank_menu():
    print("\n--- Bank Account Simulator ---")
    owner = input("Account holder name: ")
    is_savings = input("Savings account? (y/n): ").lower() == "y"
    account = SavingsAccount(owner) if is_savings else Account(owner)

    while True:
        options = "1. Deposit  2. Withdraw  3. Check balance  4. Back"
        if is_savings:
            options = options.replace("4. Back", "4. Apply interest  5. Back")
        print(f"\n{options}")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                account.deposit(float(input("Amount: ")))
            elif choice == "2":
                account.withdraw(float(input("Amount: ")))
            elif choice == "3":
                print(f"Balance: {account.balance:.2f}")
            elif choice == "4" and is_savings:
                account.apply_interest()
            elif (choice == "4" and not is_savings) or (choice == "5" and is_savings):
                break
            else:
                print("Unknown option.")
        except (InvalidAmountError, InsufficientFundsError) as e:
            print(f"Transaction failed: {e}")
        except ValueError:
            print("Please enter a valid number.")
