# 📊 Análise de Dados de Pessoas com Python

Este projeto realiza a leitura, limpeza e análise de dados de pessoas a partir de um arquivo CSV. Os dados são processados em objetos Python, validados, exportados para JSON e um relatório estatístico é gerado no terminal.

---

## 🚀 Funcionalidades

- Leitura de um arquivo CSV contendo dados de pessoas
- Criação de objetos `Pessoa` com validações
- Geração de arquivo JSON estruturado com os dados processados
- Relatório estatístico com:
  - Distribuição por gênero
  - Distribuição por região do Brasil
  - Qualidade dos dados (CPF/celular)
  - Interesses mais comuns (geral e por gênero)

---

## 🗂️ Estrutura do Projeto

09_analise_de_dados/
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
2. Instale o Python (3.10 ou superior recomendado)
3. Execute o projeto
Edite os caminhos dos arquivos no final do main.py:


if __name__ == "__main__":
    caminho_csv = "caminho/para/seu/lista_clientes.csv"
    caminho_json = "caminho/para/salvar/saida.json"
    limite = 3  # ou None para ler todo o CSV
    main(caminho_csv, caminho_json, limite)

Depois, execute:
src/main.py

📈 Exemplo de Saída

✅ Arquivo JSON salvo com sucesso: saida.json

📊 Relatório de Dados Processados:
----------------------------------------
👤 Male      : 1 pessoa(s) (33.3%)
👤 Female    : 2 pessoa(s) (66.7%)

📍 Distribuição Geográfica por Região:
  Sudeste    : 3 pessoa(s) (100.0%)

🧪 Qualidade dos Dados:
  CPFs inválidos     : 1 (33.3%)
  Celulares inválidos: 1 (33.3%)

🎯 Áreas de Interesse (geral):
  tecnologia         : 2 pessoa(s) (66.7%)
  marketing          : 1 pessoa(s) (33.3%)
✅ Requisitos
Python 3.10+

Biblioteca padrão do Python (collections, csv, json, etc.)

🧑‍💻 Autor
Eduardo Coelho

📄 Licença
Este projeto está licenciado sob a MIT License.
