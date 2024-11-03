import csv
import os
from collections import defaultdict

def save_report(report_data, filename="search_report.csv"):
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    file_path = os.path.join(reports_dir, filename)
    
    # Estrutura para acumular os valores e contar as amostragens
    aggregated_data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {
        "sequencial": {"comparisons": 0, "time": 0, "count": 0},
        "binary": {"comparisons": 0, "time": 0, "count": 0},
        "avl": {"comparisons": 0, "time": 0, "count": 0}
    })))
    
    # Agregar dados de comparação e tempo
    for row in report_data:
        size, sample, tree_type, variant, key, search_type, comparisons, time = row
        file_type = "Ordenado" if variant == "sorted" else "Nao Ordenado"
        search_type_name = "Presente" if search_type == "known" else "Nao Presente"
        
        tree_data = aggregated_data[size][file_type][search_type_name][tree_type]
        tree_data["comparisons"] += comparisons
        tree_data["time"] += time
        tree_data["count"] += 1

    # Escrever os dados no CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([
            "Tam.", "Tipo Arquivo", "Tipo Busca", 
            "Sequencial - No Comp.", "Sequencial - Tempo (ms)",
            "Arvore Binaria - No Comp.", "Arvore Binaria - Tempo (ms)",
            "AVL - No Comp.", "AVL - Tempo (ms)"
        ])
        
        for size in sorted(aggregated_data.keys()):
            for file_type in ["Ordenado", "Nao Ordenado"]:
                for search_type in ["Presente", "Nao Presente"]:
                    row_data = [size, file_type, search_type]
                    
                    for tree_type in ["sequencial", "binary", "avl"]:
                        tree_data = aggregated_data[size][file_type][search_type].get(tree_type, {})
                        if tree_data["count"] > 0:
                            avg_comparisons = tree_data["comparisons"] / tree_data["count"]
                            avg_time = tree_data["time"] / tree_data["count"]
                            row_data.extend([avg_comparisons, avg_time])
                        else:
                            row_data.extend(["-", "-"])
                    
                    writer.writerow(row_data)
    
    print(f"Report saved as {file_path}")
