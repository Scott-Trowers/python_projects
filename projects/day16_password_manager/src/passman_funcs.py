import random
import string
import json

PATH_TO_JSON = '../data/saved_details.json'

def random_pw(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string


def load_details_file():
    try:
        with open(PATH_TO_JSON, 'r') as file:
            saved_deets = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        saved_deets = {}

    return saved_deets


def update_details_file(new_entry):
    saved_deets = load_details_file()
    saved_deets.update(new_entry)

    with open(PATH_TO_JSON, 'w') as file:
        json.dump(saved_deets, file, indent=4)


def search_details_file(website):
    saved_deets = load_details_file()

    entry = saved_deets.get(website)

    return entry
