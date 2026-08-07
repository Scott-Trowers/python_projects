from art import logo
import random
from game_data import data
import time

def select_person(data):
    time.sleep(0.5)
    person1, person2 = random.sample(data, k=2)
    print(f'A) {person1["name"]}, a {person1["description"]} from {person1["country"]}?')

    time.sleep(0.5)
    print(f'B) {person2["name"]}, a {person2["description"]} from {person2["country"]}?')

    return person1["follower_count"], person2["follower_count"]


def evaluate_choice(choice, count1, count2, correct_guess):
    time.sleep(1)
    print(f"Option A has {count1} followers....")
    time.sleep(1)
    print(f"Option B has {count2} followers....")
    time.sleep(1)

    # Special messaging for draws or losses.
    if count1 == count2:
        print("Draw! Free pass!")
    elif (choice == 'a' and count1 > count2) or (choice == 'b' and count2 > count1):
        # if the user is correct, further actions are handled by the calling function.
        pass
    else:
        print("Incorrect! You Lose!")
        correct_guess = False

    return correct_guess


def higher_lower_round(stats, data):
    current_score = 0
    correct_guess = True

    while correct_guess:
        print("Who has more followers?")
        person1_followers, person2_followers = select_person(data)
        print("-------------------------")

        choice = ''
        while choice not in list('ab'):
            choice = str(input("Make your choice (A/B): ")).lower()

        correct_guess = evaluate_choice(choice, person1_followers, person2_followers, correct_guess)
        print("-------------------------")

        if correct_guess:
            current_score += 1
            print(f"Correct! Current score: {current_score}")
        else:
            print(f"Final score: {current_score}")
            stats["Games Played"] += 1
            stats["Total Score"] += current_score

            if current_score > stats["Max Score"]:
                stats["Max Score"] = current_score

            if (stats["Lowest Score"] is None) or (current_score < stats["Lowest Score"]):
                stats["Lowest Score"] = current_score

            if current_score == 0:
                stats["Out in 1"] += 1

            print("-------------------------")

    return stats


def print_stats(stats):
    print("Game Stats:")
    for item, amount in stats.items():
        print("{}: {}".format(item, amount))


def higher_or_lower(data):
    print(logo)

    stats = {
        "Games Played": 0,
        "Max Score": 0,
        "Lowest Score": None,
        "Total Score": 0,
        "Out in 1": 0
    }

    playing_game = True

    while playing_game:
        stats = higher_lower_round(stats, data)
        print_stats(stats)
        print("-------------------------")

        play_again = ""
        while play_again not in list('yn'):
            play_again = str(input("Play again? (Y/N) ").lower())

        if play_again == 'n':
            playing_game = False
            print("Thanks for playing! Goodbye!")

    return

higher_or_lower(data)
