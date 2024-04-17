#!/usr/bin/env python

from typing import Protocol

class Notifier(Protocol):
    def send_notification(self, message: str) -> None:
        pass


class EmailNotification:
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")


class SMSNotification:
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")


class Notification:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, message: str) -> None:
        self.notifier.send_notification(message)


class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance
        self.notification = EmailNotification()

    def deposit(self, amount: float) -> str:
        self.balance += amount
        return f"Deposit of {amount} made to account {self.account_number}"

    def withdraw(self, amount: float) -> str:
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal of {amount} made from account {self.account_number}"
        else:
            raise ValueError("Insufficient balance.")


def main() -> None:
    email_notification = Notification(EmailNotification())
    sms_notification = Notification(SMSNotification())
    account1 = BankAccount("1234567890", 1000.0)
    email_notification.send(account1.deposit(500.0))
    sms_notification.send(account1.withdraw(200.0))

    account2 = BankAccount("9876543210", 500.0)
    email_notification.send(account2.deposit(1000.0))
    sms_notification.send(account2.withdraw(800.0))
    

if __name__ == "__main__":
    main()
