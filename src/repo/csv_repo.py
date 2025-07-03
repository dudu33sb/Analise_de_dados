import csv
from typing import List, Dict

def ler_csv(caminho: str) -> List[Dict[str, str]]:
    
    """Lê um arquivo CSV e retorna uma lista de dicionários."""

    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return [linha for linha in leitor]
