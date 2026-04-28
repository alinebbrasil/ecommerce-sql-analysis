import sqlite3
import pandas as pd
from pathlib import Path

# Define o caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Define o caminho do banco SQLite
db_path = BASE_DIR / "ecommerce.db"

# Conecta ao banco SQLite
conn = sqlite3.connect(db_path)

# Consulta a quantidade de linhas da tabela final
query = """
SELECT
    COUNT(*) AS total_rows
FROM retail_final;
"""

# Executa a consulta
df = pd.read_sql_query(query, conn)

# Exibe o resultado
print(df.to_string(index=False))

# Fecha a conexão
conn.close()