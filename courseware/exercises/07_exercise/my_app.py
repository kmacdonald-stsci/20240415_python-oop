#!/usr/bin/env python

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, interest_rate: float):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance.")

    def calculate_interest(self) -> float:
        return self.balance * self.interest_rate


class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, balance: float):
        super().__init__(account_number, balance)

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance.")


def main() -> None:
    # Create objects and test the functionality
    savings_account = SavingsAccount("1234567890", 1000.0, 0.05)
    checking_account = CheckingAccount("9876543210", 500.0)

    print("Savings: ")
    print(savings_account.calculate_interest())
    

if __name__ == "__main__":
    main()
