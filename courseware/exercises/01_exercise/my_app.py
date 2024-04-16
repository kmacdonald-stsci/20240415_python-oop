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
        self.balance = self.balance - amount


def main() -> None:
    # Instantiate an object of the BankAccount class and test the methods
    account = BankAccount("BA00001234_01", 100.)
    print(f"Balance: ${account.balance}")
    print("    Deposit: $255")
    account.deposit(255.)
    print(f"Balance: ${account.balance}")
    print("    Withdraw: $25")
    account.withdraw(25.)
    print(f"Balance: ${account.balance}")
    

if __name__ == "__main__":
    main()
