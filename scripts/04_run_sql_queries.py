import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
db_path = BASE_DIR / "ecommerce.db"

conn = sqlite3.connect(db_path)

query = """
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS missing_customer_id,
    SUM(CASE WHEN description IS NULL THEN 1 ELSE 0 END) AS missing_description,
    SUM(CASE WHEN quantity < 0 THEN 1 ELSE 0 END) AS negative_quantity_rows,
    SUM(CASE WHEN unit_price <= 0 THEN 1 ELSE 0 END) AS invalid_unit_price_rows,
    SUM(CASE WHEN invoice_no LIKE 'C%' THEN 1 ELSE 0 END) AS cancelled_invoices
FROM retail_clean;
"""

df = pd.read_sql_query(query, conn)

print(df.to_string(index=False))

conn.close()