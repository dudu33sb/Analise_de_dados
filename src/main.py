import os
import random
from collections import Counter, defaultdict
from repo.csv_repo import ler_csv
from models.pessoa import Pessoa
from repo.json_repo import salvar_json


def main(caminho_csv: str, caminho_json: str, limite: int = None) -> None:
    """
    Função principal para processar dados de pessoas a partir de um arquivo CSV,
    salvar os dados em JSON e gerar um relatório estatístico.

    Args:
        caminho_csv (str): Caminho do arquivo CSV de entrada.
        caminho_json (str): Caminho do arquivo JSON de saída.
        limite (Optional[int]): Número máximo de pessoas a processar. Se None, processa todas.
            (Usando limite durante testes de implementação)
    """
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa terminal no Windows

    print(f"\n📥 Lendo dados do arquivo CSV: {caminho_csv}")
    dados_csv = ler_csv(caminho_csv)

    # Padroniza os cabeçalhos para lowercase para evitar problemas de chave
    dados_csv = [
        {k.lower(): v for k, v in linha.items()}
        for linha in dados_csv
    ]

    # Embaralha a lista para processamento aleatório
    #random.shuffle(dados_csv)
    #comentado para o json ser impresso em ordem. random apenas durante o teste

    if limite:
        dados_csv = dados_csv[:limite]

    print(f"👤 Processando até {limite or 'todas as'} pessoas...")
    pessoas = []

    for i, linha in enumerate(dados_csv, start=1):
        # Tenta obter o nome completo por possíveis chaves
        nome = (
            linha.get('nome_completo') or
            linha.get('nome') or
            linha.get('nomecompleto') or
            ""
        )

        if not nome.strip():
            print(f"⚠️  Linha {i} ignorada: nome ausente.")
            continue

        pessoa = Pessoa(
            nome_completo=nome,
            email=linha.get('email'),
            celular=linha.get('celular'),
            cpf=linha.get('cpf'),
            cep=linha.get('cep'),
            interesse=linha.get('interesse')
        )

        pessoas.append(pessoa)
        print(f"  ✅ Pessoa {i}: {pessoa.nome_completo} ({pessoa.genero}) processada.")

        print("\n💾 Salvando dados no arquivo JSON...")

    def gerar_relatorio(pessoas):
        """
        Gera e imprime um relatório estatístico sobre os dados processados.

        Args:
            pessoas (List[Pessoa]): Lista de objetos Pessoa processados.
        """
        print("\n📊 Relatório de Dados Processados:\n" + "-" * 40)

        total = len(pessoas)

        # 1. Distribuição de gênero
        generos = Counter(p.genero for p in pessoas)
        for genero in ["male", "female", "indefinido"]:
            qtd = generos.get(genero, 0)
            perc = (qtd / total) * 100
            print(f"👤 {genero.capitalize():<10}: {qtd} pessoa(s) ({perc:.1f}%)")

        # 2. Distribuição geográfica por região
        regioes_por_estado = {
            "AC": "Norte", "AM": "Norte", "AP": "Norte", "PA": "Norte", "RO": "Norte", "RR": "Norte", "TO": "Norte",
            "AL": "Nordeste", "BA": "Nordeste", "CE": "Nordeste", "MA": "Nordeste", "PB": "Nordeste",
            "PE": "Nordeste", "PI": "Nordeste", "RN": "Nordeste", "SE": "Nordeste",
            "DF": "Centro-Oeste", "GO": "Centro-Oeste", "MT": "Centro-Oeste", "MS": "Centro-Oeste",
            "ES": "Sudeste", "MG": "Sudeste", "RJ": "Sudeste", "SP": "Sudeste",
            "PR": "Sul", "RS": "Sul", "SC": "Sul"
        }

        regioes = Counter()
        for p in pessoas:
            estado = p.endereco.estado
            regiao = regioes_por_estado.get(estado, "Desconhecida")
            regioes[regiao] += 1
        print("\n📍 Distribuição Geográfica por Região:")
        for regiao, qtd in regioes.items():
            perc = (qtd / total) * 100
            print(f"  {regiao:<12}: {qtd} pessoa(s) ({perc:.1f}%)")

        # 3. Qualidade dos dados
        cpf_invalidos = sum("CPF inválido" in p.get_observacoes() for p in pessoas)
        celular_invalido = sum(
            any(obs in p.get_observacoes() for obs in ["Celular Vazio", "Celular Invalido"])
            for p in pessoas
        )
        print("\n🧪 Qualidade dos Dados:")
        print(f"  CPFs inválidos     : {cpf_invalidos} ({cpf_invalidos/total:.1%})")
        print(f"  Celulares inválidos: {celular_invalido} ({celular_invalido/total:.1%})")

        # 4. Áreas de interesse (geral)
        interesses = Counter(p.interesse.lower() for p in pessoas if p.interesse)
        print("\n🎯 Áreas de Interesse (geral):")
        for area, qtd in interesses.most_common():
            print(f"  {area:<20}: {qtd} pessoa(s) ({qtd/total:.1%})")

        # 5. Interesses por gênero
        interesses_por_genero = defaultdict(Counter)
        for p in pessoas:
            genero = p.genero or "indefinido"
            interesse = p.interesse.lower() if p.interesse else "nenhum"
            interesses_por_genero[genero][interesse] += 1

        print("\n📌 Interesses mais comuns por gênero:")
        for genero, interesses_mais in interesses_por_genero.items():
            print(f"\n  🔹 {genero.capitalize()}:")
            total_gen = sum(interesses_mais.values())
            for interesse, qtd in interesses_mais.most_common(3):
                perc = (qtd / total_gen) * 100 if total_gen > 0 else 0
                print(f"    - {interesse:<20}: {qtd} pessoa(s) ({perc:.1f}%)")

        print("-" * 40 + "\n✅ Fim do Relatório\n")

    salvar_json(pessoas, caminho_json)
    print(f"✅ Arquivo JSON salvo com sucesso: {caminho_json}")

    # Gera relatório estatístico
    gerar_relatorio(pessoas)



if __name__ == "__main__":
    caminho_csv = "C:/Users/SAMSUNG/Desktop/NExT/POO_com_Python/PROJETOS/09_analise_de_dados/lista_clientes.csv"
    caminho_json = "C:/Users/SAMSUNG/Desktop/NExT/POO_com_Python/PROJETOS/09_analise_de_dados/saida.json"
    limite = None # Define um limite inteiro para testar com menos dados, ou None para todos

    main(caminho_csv, caminho_json, limite)
