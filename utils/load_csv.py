import csv
import os

def load_csv(filename):
    file_path = os.path.join(os.path.dirname(__file__), '../data', filename)
    records = []
    
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = int(row[0])
            data1 = int(row[1])
            data2 = row[2]
            records.append((key, data1, data2))
    
    return records