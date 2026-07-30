# day 3 - coffee machine (procedural)

A CLI coffee machine simulator written in a procedural style. Serves espresso, latte, and cappuccino.

## how to run

```bash
uv run src/main.py
```

## features

- tracks water, milk, and coffee resources — refuses orders it can't fulfil
- coin-based payment with change returned
- `report` option to inspect current resource levels
- `power_off` option to shut down

## notes

rewritten using OOP in day 16.
