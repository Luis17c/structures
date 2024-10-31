import csv
import os

def save_report(report_data, filename="search_report.csv"):
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    file_path = os.path.join(reports_dir, filename)
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([
            "Tam.", "Tipo Arquivo", "Tipo Busca", 
            "Sequencial - No Comp.", "Sequencial - Tempo (ms)",
            "Arvore Binaria - No Comp.", "Arvore Binaria - Tempo (ms)",
            "AVL - No Comp.", "AVL - Tempo (ms)"
        ])
        
        for size in sorted(set([row[0] for row in report_data])):
            for file_type in ["Ordenado", "Nao Ordenado"]:
                for search_type in ["Presente", "Nao Presente"]:
                    variant = "sorted" if file_type == "Ordenado" else "random"
                    search_type_value = "known" if search_type == "Presente" else "unknown"
                    
                    filtered_data = [
                        row for row in report_data 
                        if row[0] == size and 
                        row[2] == variant and 
                        row[4] == search_type_value
                    ]
                    
                    print(f"Filtered data for size={size}, file_type={file_type}, search_type={search_type}")
                    
                    row_data = [size, file_type, search_type]
                    
                    for tree_type in ["sequencial", "binary", "avl"]:
                        tree_data = next(
                            (item for item in filtered_data if item[1] == tree_type), 
                            None
                        )
                        if tree_data:
                            row_data.extend([tree_data[5], tree_data[6]])
                        else:
                            row_data.extend(["-", "-"])
                    
                    writer.writerow(row_data)
    
    print(f"Report saved as {file_path}")