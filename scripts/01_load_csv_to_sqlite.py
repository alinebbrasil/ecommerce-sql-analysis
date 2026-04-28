import sqlite3
import pandas as pd
from pathlib import Path

# Define o caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Define o caminho do CSV
csv_path = BASE_DIR / "data" / "raw" / "online_retail.csv"

# Define o caminho do banco SQLite
db_path = BASE_DIR / "ecommerce.db"

# Lê o arquivo CSV
df = pd.read_csv(csv_path)

# Padroniza os nomes das colunas
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Conecta ao banco SQLite
conn = sqlite3.connect(db_path)

# Carrega os dados em uma tabela bruta
df.to_sql("retail_raw", conn, if_exists="replace", index=False)

# Fecha a conexão com o banco
conn.close()

# Exibe confirmação
print("Dataset carregado com sucesso.")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")
print(f"Banco criado em: {db_path}")