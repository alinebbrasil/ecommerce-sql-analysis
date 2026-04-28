import sqlite3
import pandas as pd
from pathlib import Path

# Define o caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Define o caminho do banco SQLite
db_path = BASE_DIR / "ecommerce.db"

# Define o caminho do arquivo SQL de métricas básicas
sql_path = BASE_DIR / "sql" / "05_basic_metrics.sql"

# Lê o conteúdo do arquivo SQL
sql_script = sql_path.read_text(encoding="utf-8")

# Separa as consultas SQL pelo ponto e vírgula
queries = [query.strip() for query in sql_script.split(";") if query.strip()]

# Conecta ao banco SQLite
conn = sqlite3.connect(db_path)

# Executa cada consulta e exibe o resultado
for index, query in enumerate(queries, start=1):
    print(f"\n--- Query {index} ---")

    # Executa a consulta SQL
    result = pd.read_sql_query(query, conn)

    # Exibe o resultado sem índice
    print(result.to_string(index=False))

# Fecha a conexão
conn.close()