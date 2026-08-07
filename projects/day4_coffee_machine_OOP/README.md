# day 4 - coffee machine (OOP)

A refactor of the day 3 coffee machine using object-oriented programming. Same behaviour, restructured into three classes.

`main.py` is written by hand. `coffee_maker.py`, `menu.py`, and `money_machine.py` are provided modules from the [100 Days of Code](https://www.udemy.com/course/100-days-of-code/) Udemy course.

## how to run

```bash
uv run src/main.py
```

## skills

- object-oriented programming — consuming pre-built classes
- class attributes, instance attributes, and methods
- modular structure across multiple files

## classes

- `CoffeeMaker` — manages resources and makes drinks
- `Menu` / `MenuItem` — models the drink options and their ingredients
- `MoneyMachine` — handles US coin-based payment (quarters, dimes, nickels, pennies)

## features

- `report` command prints current stock and profit
- `off` command shuts the machine down
- change returned automatically if overpaid
