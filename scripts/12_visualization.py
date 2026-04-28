import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Define caminhos
BASE_DIR = Path(__file__).resolve().parents[1]
db_path = BASE_DIR / "ecommerce.db"
images_path = BASE_DIR / "images"

# Estilo visual padrão
sns.set_style("white")

# Conecta ao banco
conn = sqlite3.connect(db_path)

# ===============================
# 1. Receita por país
# ===============================

query_country = """
SELECT
    country,
    SUM(total_price) AS revenue
FROM retail_final
GROUP BY country
ORDER BY revenue DESC
LIMIT 10;
"""

df_country = pd.read_sql_query(query_country, conn)

# Cria gráfico
fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(
    data=df_country,
    x="revenue",
    y="country",
    palette="Blues_r",
    ax=ax
)

# Ajustes visuais
ax.set_title("Top 10 Países por Receita", fontsize=16, weight="bold")
ax.set_xlabel("Receita")
ax.set_ylabel("")

plt.tight_layout()

# Salva imagem
fig.savefig(images_path / "revenue_by_country.png", dpi=300)

plt.close(fig)

# ===============================
# 2. Top clientes
# ===============================

query_customers = """
SELECT
    customer_id,
    SUM(total_price) AS total_spent
FROM retail_final
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
"""

df_customers = pd.read_sql_query(query_customers, conn)

fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(
    data=df_customers,
    x="total_spent",
    y="customer_id",
    palette="Blues_r",
    ax=ax
)

ax.set_title("Top 10 Clientes por Receita", fontsize=16, weight="bold")
ax.set_xlabel("Receita")
ax.set_ylabel("")

plt.tight_layout()

fig.savefig(images_path / "top_customers.png", dpi=300)

plt.close(fig)

# ===============================
# 3. Frequência de clientes
# ===============================

query_freq = """
SELECT
    CASE
        WHEN order_count = 1 THEN 'Compra única'
        ELSE 'Recorrente'
    END AS customer_type,
    COUNT(*) AS total
FROM (
    SELECT
        customer_id,
        COUNT(DISTINCT invoice_no) AS order_count
    FROM retail_final
    GROUP BY customer_id
)
GROUP BY customer_type;
"""

df_freq = pd.read_sql_query(query_freq, conn)

fig, ax = plt.subplots(figsize=(6, 6))

sns.barplot(
    data=df_freq,
    x="customer_type",
    y="total",
    palette="Blues_r",
    ax=ax
)

ax.set_title("Frequência de Clientes", fontsize=16, weight="bold")
ax.set_xlabel("")
ax.set_ylabel("Quantidade")

plt.tight_layout()

fig.savefig(images_path / "customer_frequency.png", dpi=300)

plt.close(fig)

# Fecha conexão
conn.close()

print("Gráficos gerados com sucesso.")