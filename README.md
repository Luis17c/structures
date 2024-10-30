# Projeto de Comparação de Estruturas de Dados para Busca

Este projeto compara o desempenho de diferentes estruturas de dados (Lista Sequencial, Árvore Binária e Árvore AVL) em operações de busca. São realizadas buscas em diferentes tamanhos de conjuntos de dados, com dados ordenados e não ordenados, medindo o número de comparações e o tempo de execução para cada estrutura e tipo de dado.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

project/ 
    ├── index.py # Script principal para executar o projeto 
    ├── structures/ # Pasta com as classes de estrutura de dados 
        ├── sequencial_tree.py # Implementação da lista sequencial │ 
        ├── binary_tree.py # Implementação da árvore binária │ 
        └── avl_tree.py # Implementação da árvore AVL 
    ├── functions/ # Funções auxiliares para geração e seleção de dados 
        ├── get_random_known_keys.py # Função para selecionar chaves conhecidas 
        ├── get_random_unknown_keys.py # Função para selecionar chaves desconhecidas │ └── random_data_generator.py # Função para gerar dados aleatórios 
    ├── utils/ # Utilitários para carregar e salvar dados 
        ├── load_csv.py # Função para carregar dados de arquivos CSV 
        └── save_report.py # Função para salvar o relatório no formato especificado
    ├── data/ # Pasta onde os registros serão armazenados 
    └── reports/ # Pasta onde o relatório final será salvo

## Requisitos

Antes de executar o projeto, você precisará instalar o Python (3.6 ou superior)

### Instalação

1. Clone este repositório em sua máquina:
    ```bash
    git clone <URL do repositório>
    cd project
    ```

Certifique-se de estar no diretório raiz do projeto.

Execute o script principal:
    ```bash
        python index.py
    ```
    
Isso irá:

Gerar arquivos CSV com diferentes tamanhos de dados (100, 500, 1000, 5000, 10000).
Preencher as estruturas de dados com dados aleatórios e ordenados.
Realizar buscas por chaves conhecidas e desconhecidas para cada estrutura.
Salvar o relatório final no diretório reports no formato search_report.csv.
Verificar o Relatório: O relatório será salvo no diretório reports com o nome search_report.csv. Este arquivo contém informações sobre o número de comparações e o tempo (em milissegundos) para cada busca, conforme especificado.

# Estrutura do Relatório
O relatório search_report.csv segue o seguinte formato:

Tam.	Tipo Arquivo	Tipo Busca	Sequencial - No Comp.	Sequencial - Tempo (ms)	Árvore Binária - No Comp.	Árvore Binária - Tempo (ms)	AVL - No Comp.	AVL - Tempo (ms)
100	Ordenado	Presente	...	...	...	...	...	... ...	...	...	...
100	Ordenado	Não Presente	...	...	...	...	...	... 	...	...	...	...	...

# Observações

O projeto utiliza time.perf_counter() para obter uma medição precisa do tempo de execução em milissegundos.

Os dados de comparação e tempo são apresentados no relatório, permitindo uma análise de desempenho entre as estruturas.
