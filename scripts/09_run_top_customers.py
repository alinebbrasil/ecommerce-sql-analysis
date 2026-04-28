import sqlite3
import pandas as pd
from pathlib import Path

# Define o caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Define o caminho do banco SQLite
db_path = BASE_DIR / "ecommerce.db"

# Define o caminho do arquivo SQL (top clientes)
sql_path = BASE_DIR / "sql" / "07_top_customers.sql"

# Lê o conteúdo da query SQL
query = sql_path.read_text(encoding="utf-8")

# Conecta ao banco SQLite
conn = sqlite3.connect(db_path)

# Executa a query e armazena o resultado em um DataFrame
df = pd.read_sql_query(query, conn)

# Exibe o resultado no terminal
print(df.to_string(index=False))

# Fecha a conexão com o banco
conn.close()