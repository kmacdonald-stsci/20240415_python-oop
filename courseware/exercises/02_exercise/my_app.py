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


class SavingsAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)
        # if amount < 0.01:
        #     raise ValueError("Amount is invalid, must be a penny or more.")
        # if amount > self.balance:
        #     raise ValueError("Insufficient funds.")
        # self.balance -= amount
        self.balance *= 1.02


class CheckingAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        total_amount = amount + 1
        if total_amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= total_amount

def perform_transactions(account: BankAccount) -> None:
    account.deposit(1000)
    account.withdraw(500)
    account.display_balance()

def main() -> None:
    # SavingsAccount("SA001", 1000),
    
    accounts: list[BankAccount] = [
        SavingsAccount("SA12345001", 1000),
        CheckingAccount("CA12345001", 1000),
        BankAccount("BA12345001", 1000)
    ]

    for account in accounts:
        print(f"Performing transactions for {type(account).__name__}:")
        perform_transactions(account)
        print()
    

if __name__ == "__main__":
    main()
