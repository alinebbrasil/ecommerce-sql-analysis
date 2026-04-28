import pandas as pd
from pathlib import Path

# Define o caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Caminho do arquivo Excel original
excel_path = BASE_DIR / "data" / "raw" / "Online Retail.xlsx"

# Caminho do CSV que será gerado
csv_path = BASE_DIR / "data" / "raw" / "online_retail.csv"

# Lê o arquivo Excel
df = pd.read_excel(excel_path)

# Salva como CSV
df.to_csv(csv_path, index=False)

# Confirmação
print("Arquivo convertido com sucesso!")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")