import sqlite3
from pathlib import Path

# Define caminho base
BASE_DIR = Path(__file__).resolve().parents[1]

# Caminho do banco
db_path = BASE_DIR / "ecommerce.db"

# Caminho do SQL
sql_path = BASE_DIR / "sql" / "01_create_clean_table.sql"

# Lê o script SQL
sql_script = sql_path.read_text(encoding="utf-8")

# Conecta ao banco
conn = sqlite3.connect(db_path)

# Executa o SQL
conn.executescript(sql_script)

# Salva e fecha
conn.commit()
conn.close()

print("Tabela retail_clean criada com sucesso.")