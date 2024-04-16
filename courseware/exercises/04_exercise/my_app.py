#!/usr/bin/env python

class BankAccount:
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

    @property
    def account_number(self) -> str:
        return self._account_number.upper()

    @account_number.setter
    def account_number(self, value: str) -> None:
        self._account_number = value

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        self._balance = value

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.balance -= amount


class BankAccountValidator(BankAccount):
    def __init__(self, account_number: str, balance: float) -> None:
        if not (isinstance(account_number, str) and len(account_number) == 10):
            raise ValueError("Invalid account number.")
        if not (isinstance(balance, (int, float)) and balance >= 0):
            raise ValueError("Invalid balance.")
        super().__init__(account_number, balance)

    def deposit(self, amount: float) -> None:
        if not (isinstance(amount, (int, float)) and amount > 0):
            raise ValueError("Invalid deposit amount.")
        super().deposit(amount)

    def withdraw(self, amount: float) -> None:
        if not (isinstance(amount, (int, float)) and 0 < amount <= self.balance):
            raise ValueError("Invalid withdrawal amount.")
        super().withdraw(amount)


'''
Eric created two independent classes and replaced the checks in the
BankAccount class with BankAccountValidator class.
'''


def main() -> None:
    # account = BankAccount("1234567890", 1000)
    account = BankAccountValidator("1234567890", 1000)
    account.deposit(500)
    # account.deposit(-500)
    account.withdraw(200)
    # account.withdraw(-200)
    print(account.balance)
    

if __name__ == "__main__":
    main()
