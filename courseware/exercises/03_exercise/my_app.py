#!/usr/bin/env python

class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Email: {self.email}")


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
    def __init__(
            self,
            account_number: str,
            balance: float,
            interest_rate: float
            customer: Customer,
    ) -> None:
        super().__init__(account_number, balance, customer)
        self.interest_rate = interest_rate

    def deposit(self):
        iamt = self.balance * (self.compound)
        self.balance = self.balance + iamt


def main() -> None:
    joe = Customer("Joe", "jdiddy@nothing.biz", 5.)
    joe_ba = SavingsAccount("AC001", 100., joe)
    print(f"Joe deposit: {joe_ba.balance}")
    joe_ba.deposit(50.)
    print(f"Joe deposit: {joe_ba.balance}")
    

if __name__ == "__main__":
    main()
