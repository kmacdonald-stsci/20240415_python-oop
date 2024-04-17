#!/usr/bin/env python

from pathlib import Path
import json
import os
import yaml

class Dumper:
    def __init__(self, file_name):
        fname, fext = os.path.splitext(file_name)
        if fext == ".json":
            self.dumper = json.dumps
        elif fext == ".yaml":
            self.dumper = yaml.dump


class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age}"
    
    def save_to_file(self, file_name: Path) -> None:
        dumper = Dumper(file_name)
        file_name.write_text(dumper.dumper(self.__dict__))


def main() -> None:
    person = Person("John", "Doe", 30)
    person.save_to_file(Path("my_person.yaml"))
    person.save_to_file(Path("my_person.json"))


if __name__ == "__main__":
    main()
