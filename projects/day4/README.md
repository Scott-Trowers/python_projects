# day 16 - coffee machine (OOP)

A refactor of the day 3 coffee machine using object-oriented programming. Same behaviour, restructured into three classes.

## how to run

```bash
uv run src/main.py
```

## classes

- `CoffeeMaker` — manages resources and makes drinks
- `Menu` / `MenuItem` — models the drink options and their ingredients
- `MoneyMachine` — handles US coin-based payment (quarters, dimes, nickels, pennies)

## features

- `report` command prints current stock and profit
- `off` command shuts the machine down
- change returned automatically if overpaid
