import random
from art import logo
import time

def take_bets():
    bet = 0
    while bet <= 0:
        try:
            bet = int(input("Place your bets! Whole pounds only! £"))
        except ValueError:
            print("Please enter an integer amount!")

    return bet


def deal_cards(deck):
    users_hand = random.choices(deck, k=2)
    dealers_hand = random.choices(deck, k=2)

    print(f"Your hand: {users_hand}")
    print(f"Dealer's hand: [{dealers_hand[0]}, |?|]")

    return users_hand, dealers_hand


def evaluate_hand(hand):
    score = sum(hand)

    if score == 21:
        print("Score: 21! Blackjack!")
    elif score < 21:
        print(f"Score: {score}")
    else:
        # ace is worth 11 by default, but can be a 1 if the hand would otherwise be bust
        while score > 21 and 11 in hand:
            hand[hand.index(11)] = 1
            score = sum(hand)
        print(f"Score: {score}")

    if score > 21:
        print(f"!!BUST!!")
        # convert a bust to 0 for easier score comparison and stat tracking
        score = 0

    return score


def users_turn(user_hand, deck):
    turn_ended = False

    while not turn_ended:
        user_score = evaluate_hand(hand=user_hand)

        # 0 represents bust
        if user_score == 0:
            turn_ended = True
            return user_score, user_hand
        elif user_score == 21:
            turn_ended = True
            return user_score, user_hand
        else:
            stick_or_twist = ""
            while stick_or_twist not in list('st'):
                stick_or_twist = str(input(f"Do you want to stick (S) or twist (T)? ")).lower()

            if stick_or_twist == "t":
                time.sleep(1)
                user_hand.append(random.choice(deck))
                print(user_hand)
                time.sleep(1)
            elif stick_or_twist == "s":
                turn_ended = True
                return user_score, user_hand


def result(user_score, dealers_score, bid, game_stats):
    # user bust or lost
    if user_score == 0 or (user_score < dealers_score):
        print(f"You lost {bid}!")
        game_stats["total_profit"] -= bid
        game_stats["games_played"] += 1
        game_stats["games_lost"] += 1

        if user_score == 0:
            game_stats["busts"] += 1

    # dealer bust
    if dealers_score == 0:
        print(f"Dealer Bust! You win {bid}!")
        game_stats["total_profit"] += bid
        game_stats["games_played"] += 1
        game_stats["games_won"] += 1
    # draw
    elif user_score == dealers_score:
        print("DRAW!")
        game_stats["games_played"] += 1
        game_stats["games_drawn"] += 1
    # user won
    elif user_score > dealers_score:
        print(f"You win {bid}!")
        game_stats["total_profit"] += bid
        game_stats["games_played"] += 1
        game_stats["games_won"] += 1

    return game_stats


def dealers_turn(dealers_hand, deck):
    print(f"Dealer's hand: {dealers_hand}")

    dealers_score = evaluate_hand(dealers_hand)

    # if the dealer isn't bust (and therefore has a score of 0) they must 'twist' until scoring over 16
    while dealers_score <= 16 and dealers_score != 0:
        time.sleep(1)
        dealers_hand.append(random.choice(deck))
        print(dealers_hand)
        time.sleep(1)
        dealers_score = evaluate_hand(dealers_hand)

    return dealers_score, dealers_hand


def blackjack_round(deck, game_stats):
    bet = take_bets()
    print(f"That's £{bet} on the table! Let's play Blackjack!")
    print("-------------------------------------------------")
    time.sleep(1)

    user_hand, dealers_hand = deal_cards(deck=deck)

    print("-------------------------------------------------")
    time.sleep(1)

    user_score, user_hand = users_turn(user_hand, deck)

    print("-------------------------------------------------")
    time.sleep(1)

    if user_score == 0:
        # dealers_score = 1 is a dummy variable, because the user is bust before the dealers turn.
        game_stats = result(user_score, dealers_score = 1, game_stats = game_stats, bid=bet)
        return game_stats

    dealers_score, dealers_hand = dealers_turn(dealers_hand, deck)

    print("-------------------------------------------------")
    time.sleep(1)

    game_stats = result(user_score, dealers_score = dealers_score, game_stats = game_stats, bid=bet)

    return game_stats


def blackjack(deck):
    print(logo)

    game_stats = {
        "total_profit": 0,
        "games_played": 0,
        "games_won": 0,
        "games_lost": 0,
        "games_drawn": 0,
        "busts": 0,
    }

    print("Welcome to the Python Casino!")

    while True:
        game_stats = blackjack_round(deck, game_stats)

        print("-------------------------------------------------")
        print("GAME STATS:")
        for stat, value in game_stats.items():
            stat_label = stat.replace('_', ' ').title()
            print("{}: {}".format(stat_label, value))
        print("-------------------------------------------------")

        play_again =  ''
        while play_again not in 'yn':
            play_again = str(input("Would you like to play again? (Y/N) ")).lower()

        if play_again == 'n':
            return game_stats


blackjack(deck=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
