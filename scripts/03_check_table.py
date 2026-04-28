import sqlite3
import pandas as pd
from pathlib import Path

# Caminho base
BASE_DIR = Path(__file__).resolve().parents[1]

# Caminho do banco
db_path = BASE_DIR / "ecommerce.db"

# Conecta ao banco
conn = sqlite3.connect(db_path)

# Query de verificação
query = "SELECT COUNT(*) AS total_linhas FROM retail_clean;"

# Executa a query
df = pd.read_sql_query(query, conn)

# Mostra resultado
print(df)

# Fecha conexão
conn.close()