import json

def salvar_json(pessoas: list, caminho: str) -> None:
    """
    Salva uma lista de objetos do tipo Pessoa em um arquivo JSON.

    Cada objeto é convertido em um dicionário com seus atributos relevantes,
    incluindo endereço e observações. Os dados são ordenados pelo nome completo
    antes de serem salvos.

    Args:
        pessoas (List[object]): Lista de objetos Pessoa.
        caminho (str): Caminho do arquivo onde os dados JSON serão salvos.

    Returns:
        None
    """

    usuarios = []

    # Constrói dicionários com os dados de cada pessoa
    for pessoa in pessoas:
        usuarios.append({
            "nome_completo": pessoa.nome_completo,
            "primeiro_nome": pessoa.primeiro_nome,
            "segundo_nome": pessoa.segundo_nome,
            "genero": pessoa.genero,
            "email": pessoa.email,
            "celular": pessoa.celular,
            "interesse": pessoa.interesse,
            "cpf": pessoa.cpf,
            "bairro": pessoa.endereco.bairro,
            "cidade": pessoa.endereco.cidade,
            "estado": pessoa.endereco.estado,
            "observacoes": ", ".join(pessoa.get_observacoes())
        })

    # Ordena os usuários pelo nome completo
    usuarios_ordenados = sorted(usuarios, key=lambda x: x["nome_completo"])

    # Salva os dados em um arquivo JSON com indentação e codificação adequada
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump({"users": usuarios_ordenados}, f, ensure_ascii=False, indent=2)
