# src/repo/json_repo.py

import json

def salvar_json(pessoas: list, caminho: str):
    """
    Salva uma lista de objetos Pessoa em um arquivo JSON, ordenados pelo nome completo.
    """
    usuarios = []

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

    # Ordena por nome completo
    usuarios_ordenados = sorted(usuarios, key=lambda x: x["nome_completo"])

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump({"users": usuarios_ordenados}, f, ensure_ascii=False, indent=2)
