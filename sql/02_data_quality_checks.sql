-- Conta o total de linhas da tabela tratada
SELECT
    COUNT(*) AS total_rows
FROM retail_clean;

-- Verifica registros sem CustomerID
SELECT
    COUNT(*) AS missing_customer_id
FROM retail_clean
WHERE customer_id IS NULL;

-- Verifica registros sem descrição do produto
SELECT
    COUNT(*) AS missing_description
FROM retail_clean
WHERE description IS NULL;

-- Verifica registros com quantidade negativa
SELECT
    COUNT(*) AS negative_quantity_rows
FROM retail_clean
WHERE quantity < 0;

-- Verifica registros com preço unitário menor ou igual a zero
SELECT
    COUNT(*) AS invalid_unit_price_rows
FROM retail_clean
WHERE unit_price <= 0;

-- Verifica faturas de cancelamento
SELECT
    COUNT(*) AS cancelled_invoice_rows
FROM retail_clean
WHERE invoice_no LIKE 'C%';

-- Verifica possíveis duplicidades
SELECT
    invoice_no,
    stock_code,
    description,
    quantity,
    invoice_date,
    unit_price,
    customer_id,
    country,
    COUNT(*) AS duplicate_count
FROM retail_clean
GROUP BY
    invoice_no,
    stock_code,
    description,
    quantity,
    invoice_date,
    unit_price,
    customer_id,
    country
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;