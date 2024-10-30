import time

from structures.sequencial_tree import SequentialTree
from structures.binary_tree import BinaryTree
from structures.avl_tree import AVLTree

from functions.get_random_known_keys import pick_known_keys
from functions.get_random_unknown_keys import pick_unknown_keys
from functions.random_data_generator import generate_csv

from utils.load_csv import load_csv
from utils.save_report import save_report

def main():
    sizes = [100, 500, 1000, 5000, 10000]
    report_data = []

    for size in sizes:
        print(f"Generating CSV files with {size} records...")
        generate_csv(size)
        print(f"CSV files for size {size} generated!")

        randomFilename = f"random_data_{size}.csv"
        sortedFilename = f"sorted_data_{size}.csv"

        print(f"Loading data from {randomFilename} and {sortedFilename}...")
        randomRecords = load_csv(randomFilename)
        sortedRecords = load_csv(sortedFilename)
        print("Data loaded successfully.")

        trees = {
            'sequencial': {
                'random': SequentialTree(),
                'sorted': SequentialTree()
            },
            'binary': {
                'random': BinaryTree(),
                'sorted': BinaryTree()
            },
            'avl': {
                'random': AVLTree(),
                'sorted': AVLTree()
            }
        }

        print(f"Populating trees for random data of size {size}...")
        for record in randomRecords:
            key, data1, data2 = record
            trees['sequencial']['random'].insert(key, data1, data2)
            trees['binary']['random'].insert(key, data1, data2)
            trees['avl']['random'].root = trees['avl']['random'].insert(trees['avl']['random'].root, key, data1, data2)
        print("Trees populated with random data.")

        print(f"Populating trees for sorted data of size {size}...")
        for record in sortedRecords:
            key, data1, data2 = record
            trees['sequencial']['sorted'].insert(key, data1, data2)
            trees['binary']['sorted'].insert(key, data1, data2)
            trees['avl']['sorted'].root = trees['avl']['sorted'].insert(trees['avl']['sorted'].root, key, data1, data2)
        print("Trees populated with sorted data.")

        print("Selecting known and unknown keys for search tests...")
        knownKeys = pick_known_keys(randomRecords)
        unknownKeys = pick_unknown_keys(randomRecords)
        print("Keys selected.", knownKeys, unknownKeys)

        for tree_type, tree_variants in trees.items():
            for variant, tree in tree_variants.items():
                root = tree.root if tree_type == 'avl' else None
                print(f"Testing known keys in {tree_type} tree with {variant} data...")

                for key in knownKeys:
                    start_time = time.perf_counter()
                    _, comparisons = tree.search_with_count(root, key)
                    elapsed_time = (time.perf_counter() - start_time) * 1000
                    report_data.append([size, tree_type, variant, key, "known", comparisons, elapsed_time])

                print(f"Testing unknown keys in {tree_type} tree with {variant} data...")

                for key in unknownKeys:
                    start_time = time.perf_counter()
                    _, comparisons = tree.search_with_count(root, key)
                    elapsed_time = (time.perf_counter() - start_time) * 1000
                    report_data.append([size, tree_type, variant, key, "unknown", comparisons, elapsed_time])
    
    print("Saving report to /reports folder...")
    save_report(report_data)
    print("Report saved successfully!")

if __name__ == "__main__":
    main()



        
        


        