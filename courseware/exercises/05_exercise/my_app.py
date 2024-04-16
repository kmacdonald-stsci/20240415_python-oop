#!/usr/bin/env python

class BankAccount:
    def __init__(self, account_number: str, balance: float) -> None:
        # Initialize account_number and balance attributes
        self.account_number = account_number 
        self.balance = balance

    # Define getter and setter methods for account_number and balance
    @property
    def account_number(self) -> str:
        return self.__account_number.upper()

    @account_number.setter
    def account_number(self, value: str) -> None:
        if len(value) < 10:
            raise ValueError(
                "Account number must be at least 10 characters long."
            )
        self.__account_number = value

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    def deposit(self, amount: float) -> None:
        # Implement the deposit method
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        self.balance = self.balance + amount

    def withdraw(self, amount: float) -> None:
        # Implement the withdraw method
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

    def display_balance(self) -> None:
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")

    def calc_interest(self):
        print("Not implemented")


class SavingsAccount(BankAccount):
    def calc_interest(self):
        interest_rate = 0.05
        interest = self.balance * interest_rate
        return interest


class CheckingAccount(BankAccount):
    def calc_interest(self):
        interest_rate = 0.02
        interest = self.balance * interest_rate
        return interest


def calculate_interest(account):
    return account.calc_interest()


def main() -> None:
    # savings_account = BankAccount("1234567890", 1000)
    # checking_account = BankAccount("9876543210", 500)
    savings_account = SavingsAccount("1234567890", 1000)
    checking_account = CheckingAccount("9876543210", 500)

    # savings_interest = calculate_interest(savings_account, "savings")
    # checking_interest = calculate_interest(checking_account, "checking")
    savings_interest = calculate_interest(savings_account)
    checking_interest = calculate_interest(checking_account)

    print(f"Savings account interest: {savings_interest}")
    print(f"Checking account interest: {checking_interest}")

    
if __name__ == "__main__":
    main()
