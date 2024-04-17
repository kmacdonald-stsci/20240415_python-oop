#!/usr/bin/env python

class Pizza:
    size: str
    crust: str
    sauce: str
    cheese: str
    toppings: list[str]

    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.sauce = None
        self.cheese = None

    def __str__(self):
        delim = " || "
        ostr = f"{self.size:15s}"
        ostr += f"{delim}{self.crust:15s}"
        ostr += f"{delim}{self.sauce:15s}"
        ostr += f"{delim}{self.cheese:20s}"
        ostr += f"{delim}{self.toppings}"
        return ostr

'''
pizza1 = Pizza("large", "thin", ["pepperoni", "mushrooms"], "tomato", "mozzarella")
pizza2 = Pizza("medium", "thick", ["ham", "pineapple"], "bbq", "cheddar")
pizza3 = Pizza("small", "regular", ["olives", "onions", "peppers"], "marinara", "parmesan")
'''

class PizzaNew:
    def __init__(self) -> None:
        self.pizza = Pizza()
        self.pizza.size = "large"
        self.pizza.crust = "regular"
        self.pizza.toppings = []
        self.pizza.sauce = "tomato"
        self.pizza.cheese = "mozzerella"

    def add_size(self, size: str) -> None:
        self.pizza.size = f"Size: {size}"

    def add_crust(self, crust: str) -> None:
        self.pizza.crust = f"Crust: {crust}"

    def add_toppings(self, toppings: list[str]) -> None:
        topping = ", ".join(toppings)
        self.pizza.toppings = f"Toppings: '{topping}'"

    def add_sauce(self, sauce: str) -> None:
        self.pizza.sauce = f"Sauce: {sauce}"

    def add_cheese(self, cheese: str) -> None:
        self.pizza.cheese = f"Cheese: {cheese}"

    def build(self):
        return self.pizza


p1 = PizzaNew()
p1.add_size("medium")
p1.add_crust("thin")
p1.add_sauce("white")
p1.add_cheese("mozzerella")
p1.add_toppings(["pepperoni", "parmesan"])
pizza1 = p1.build()

p2 = PizzaNew()
p2.add_size("medium")
p2.add_crust("thick")
p2.add_sauce("bbq")
p2.add_cheese("cheddar")
p2.add_toppings(["ham", "pineapple"])
pizza2 = p2.build()

p3 = PizzaNew()
p3.add_size("small")
p3.add_crust("regular")
p3.add_sauce("marinara")
p3.add_cheese("parmesan")
p3.add_toppings(["olives", "onions", "peppers"])
pizza3 = p3.build()

print(pizza1)
print(pizza2)
print(pizza3)
