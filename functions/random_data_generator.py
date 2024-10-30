import csv
import random
import string
import os

def generate_csv(size):
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    os.makedirs(data_dir, exist_ok=True)

    records = []
    for i in range(size):
        key = i + 1
        data1 = random.randint(1, 10000)
        data2 = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
        records.append([key, data1, data2])

    random_filename = os.path.join(data_dir, f"random_data_{size}.csv")
    with open(random_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["key", "data1", "data2"])
        writer.writerows(records)

    sorted_filename = os.path.join(data_dir, f"sorted_data_{size}.csv")
    records_sorted = sorted(records, key=lambda x: x[1])
    with open(sorted_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["key", "data1", "data2"])
        writer.writerows(records_sorted)
