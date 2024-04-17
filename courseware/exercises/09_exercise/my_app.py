#!/usr/bin/env python

class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        return (f"{self.street}\n"
                f"{self.city}, {self.state} {self.zip_code}")


class Person:
    def __init__(
      self, first_name: str, last_name: str, street: str,
      city: str, state: str, zip_code: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.address = Address(street, city, state, zip_code)

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}\n"
                f"{self.address.street}\n"
                f"{self.address.city}, {self.address.state} {self.address.zip_code}")


class PersonNew:
    def __init__(self, first_name: str, last_name: str, addr: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = addr

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}\n"
                f"{self.address}")



def main() -> None:
    addr = Address("123 Elm St", "Springfield", "IL", "62701")
    person = PersonNew("John", "Doe", addr)
    #   "John", "Doe", "123 Elm St", "Springfield", "IL", "62701")
    print(person)
    

if __name__ == "__main__":
    main()
