# 📊 Análise de Dados de Pessoas com Python

Este projeto realiza a leitura, limpeza e análise de dados de pessoas a partir de um arquivo CSV. Os dados são processados em objetos Python, validados, exportados para JSON e um relatório estatístico é gerado no terminal.

---

## 🚀 Funcionalidades

- Leitura de um arquivo CSV contendo dados de pessoas
- Criação de objetos `Pessoa` com validações de CPF, celular e endereço
- Normalização e formatação de dados (nome, CPF, telefone, CEP)
- Geração de arquivo JSON estruturado com os dados processados
- Relatório estatístico detalhado:
  - Distribuição por gênero (masculino, feminino, indefinido)
  - Distribuição por região do Brasil (Norte, Nordeste, Sudeste, Sul, Centro-Oeste)
  - Avaliação da qualidade dos dados (validação de CPF e celular)
  - Interesses mais comuns, no geral e segmentados por gênero

---

## 🗂️ Estrutura do Projeto

analise_de_dados/
├── src/
│ ├── main.py           
│ ├── models/
│ │ └── pessoa.py
│ └── repo/
│ ├── csv_repo.py
│ └── json_repo.py
├── lista_clientes.csv
└── saida.json

---

## 📌 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/09_analise_de_dados.git
cd 09_analise_de_dados

```
2. Instale o Python (3.10 ou superior recomendado)

3. Execute o projeto
Edite os caminhos dos arquivos no final do arquivo src/main.py:

if __name__ == "__main__":
    caminho_csv = "caminho/para/seu/lista_clientes.csv"
    caminho_json = "caminho/para/salvar/saida.json"
    limite = 3  # ou None para ler todo o CSV
    main(caminho_csv, caminho_json, limite)

Depois, execute o script:

python src/main.py


🧩 Detalhes das Principais Classes e Módulos

models.pessoa.Pessoa
Classe principal que representa uma pessoa com:

Normalização e validação do nome completo (capitalização e preposições)

Validação e formatação do CPF (inclui verificação de dígitos)

Normalização e validação do celular (inclui DDD automático baseado no CEP)

Consulta e normalização do endereço via CEP

Registro de observações sobre dados inválidos ou inconsistências

repo.csv_repo
Funções para ler o arquivo CSV e transformar em lista de dicionários ou objetos Pessoa.

repo.json_repo
Funções para exportar os dados processados para JSON, com ordenação e estrutura adequada para relatórios.

src/main.py
Ponto de entrada do programa que coordena:

Leitura dos dados CSV

Processamento e validação dos objetos Pessoa

Exportação para JSON

Impressão do relatório estatístico no terminal

📈 Exemplo de Saída

✅ Arquivo JSON salvo com sucesso: saida.json

📊 Relatório de Dados Processados:
----------------------------------------
👤 Male      : 10 pessoa(s) (33.3%)
👤 Female    : 20 pessoa(s) (66.7%)
👤 Indefinido: 0 pessoa(s) (0.0%)

📍 Distribuição Geográfica por Região:
  Sudeste    : 15 pessoa(s) (50.0%)
  Nordeste   : 10 pessoa(s) (33.3%)
  Sul        : 5 pessoa(s)  (16.7%)

🧪 Qualidade dos Dados:
  CPFs inválidos     : 2 (6.7%)
  Celulares inválidos: 3 (10.0%)

🎯 Áreas de Interesse (geral):
  tecnologia         : 12 pessoa(s) (40.0%)
  marketing          : 8 pessoa(s)  (26.7%)
  vendas             : 10 pessoa(s) (33.3%)

🧪 Testes
O projeto inclui testes unitários para as principais funcionalidades:

Validação de CPF

Normalização de nomes e celulares

Validação e consulta de endereço

Inferência de gênero

Para executar os testes:
python -m unittest discover -s tests


✅ Requisitos
Python 3.10+

Bibliotecas padrão do Python (collections, csv, json, etc.)

🧑‍💻 Autor
Eduardo Coelho
