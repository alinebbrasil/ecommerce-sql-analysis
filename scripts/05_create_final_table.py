import sqlite3
from pathlib import Path

# Define o caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Define o caminho do banco SQLite
db_path = BASE_DIR / "ecommerce.db"

# Define o caminho do SQL que cria a tabela final
sql_path = BASE_DIR / "sql" / "04_create_final_table.sql"

# Lê o conteúdo do arquivo SQL
sql_script = sql_path.read_text(encoding="utf-8")

# Conecta ao banco SQLite
conn = sqlite3.connect(db_path)

# Executa o script SQL
conn.executescript(sql_script)

# Salva as alterações
conn.commit()

# Fecha a conexão
conn.close()

# Exibe confirmação
print("Tabela retail_final criada com sucesso.")