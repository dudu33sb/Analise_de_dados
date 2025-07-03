# Projeto de Normalização de Dados de Usuários

## Descrição

Este projeto lê um arquivo CSV com dados de usuários, normaliza e valida informações como nome, CPF, celular e CEP, infere gênero pelo primeiro nome via API pública, e gera um arquivo JSON organizado com os dados tratados.

---

## Como usar


### Pré-requisitos

- Python 3.7+
- Instalar dependências (requests, pytest):

bash
pip install requests pytest



API de Gênero
Usamos a API gratuita genderize.io para inferir o gênero pelo primeiro nome.

Observações
Celular é normalizado para o formato DD 9XXXXXXXX.

CPF é validado e formatado (apenas números).

CEP é usado para buscar bairro, cidade e estado via API ViaCEP.

Problemas encontrados são adicionados no campo observacoes do JSON.


Estrutura do projeto
src/models/: Modelos de dados (Pessoa, CPF, Endereco)

src/services/: Serviços auxiliares (validação de CPF, consulta de gênero)

src/repo/: Repositórios para ler CSV e salvar JSON

src/main.py: Script principal

tests/: Testes unitários

Autor
Eduardo Coelho - 2025