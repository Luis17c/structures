import random

def pick_known_keys(records, count=15):
    existing_keys = [record[0] for record in records]
    return random.sample(existing_keys, count)