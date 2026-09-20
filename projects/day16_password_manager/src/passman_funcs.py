import random
import string
import json

PATH_TO_JSON = '../data/saved_details.json'

def random_pw(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string

def save_to_file(new_entry):
    with open(PATH_TO_JSON, 'r+') as f:
        try:
            dic = json.load(f)
        except json.decoder.JSONDecodeError:
            dic = {}
        dic.update(new_entry)
        f.seek(0)
        json.dump(dic, f)
        f.truncate()
