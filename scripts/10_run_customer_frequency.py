import sqlite3
import pandas as pd
from pathlib import Path

# Caminhos do projeto
BASE_DIR = Path(__file__).resolve().parents[1]
db_path = BASE_DIR / "ecommerce.db"
sql_path = BASE_DIR / "sql" / "08_customer_frequency.sql"

# Conecta ao banco
conn = sqlite3.connect(db_path)

# Lê e executa a query
query = sql_path.read_text(encoding="utf-8")
df = pd.read_sql_query(query, conn)

# Exibe resultado
print(df.to_string(index=False))

# Fecha conexão
conn.close()