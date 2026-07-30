# day 1 - blackjack

A CLI blackjack game with betting in pounds, played against a simple dealer AI.

## how to run

```bash
uv run src/main.py
```

## skills

- functions and control flow
- dictionaries for tracking session state
- error handling with `try/except`
- `random` module

## features

- place a bet before each round (whole pounds only)
- aces count as 11 but automatically drop to 1 to avoid busting
- dealer hits on 16 or under, stands on 17+
- tracks session stats: games played, won, lost, drawn, total busts, and total profit/loss
