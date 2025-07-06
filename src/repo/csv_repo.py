import csv
from typing import List, Dict

def ler_csv(caminho: str) -> List[Dict[str, str]]:
    """
    Lê um arquivo CSV e retorna seu conteúdo como uma lista de dicionários.

    Cada linha do CSV é convertida em um dicionário onde:
        - as chaves são os nomes das colunas (definidos na primeira linha do arquivo),
        - os valores são os dados correspondentes de cada linha.

    Args:
        caminho (str): Caminho para o arquivo CSV a ser lido.

    Returns:
        List[Dict[str, str]]: Lista de dicionários com os dados do CSV.
                              Cada dicionário representa uma linha do arquivo.
    """    

    # Abre o arquivo CSV no modo leitura e com codificação UTF-8
    with open(caminho, mode='r', encoding='utf-8') as arquivo:

        # Usa DictReader para transformar cada linha em um dicionário
        leitor = csv.DictReader(arquivo)

        # Retorna uma lista com todas as linhas convertidas
        return [linha for linha in leitor]
