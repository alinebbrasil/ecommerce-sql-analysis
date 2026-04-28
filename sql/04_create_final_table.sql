-- Remove tabela final se já existir
DROP TABLE IF EXISTS retail_final;

-- Cria tabela limpa para análise
CREATE TABLE retail_final AS
SELECT
    invoice_no,
    stock_code,
    description,
    quantity,
    invoice_date,
    unit_price,
    customer_id,
    country,
    quantity * unit_price AS total_price

FROM retail_clean

WHERE
    customer_id IS NOT NULL
    AND unit_price > 0
    AND quantity > 0;