import random

def pick_unknown_keys(records, count=15):
    existing_keys = {record[0] for record in records}
    max_key = max(existing_keys)
    unknown_keys = []
    
    while len(unknown_keys) < count:
        new_key = random.randint(max_key + 1, max_key + 10000)
        if new_key not in existing_keys and new_key not in unknown_keys:
            unknown_keys.append(new_key)
    
    return unknown_keys