-- Remove tabela tratada se já existir
DROP TABLE IF EXISTS retail_clean;

-- Cria tabela tratada a partir da tabela bruta
CREATE TABLE retail_clean AS
SELECT
    -- Identificador da fatura
    InvoiceNo AS invoice_no,

    -- Código e descrição do produto
    StockCode AS stock_code,
    Description AS description,

    -- Quantidade (pode ser negativa em cancelamentos)
    Quantity AS quantity,

    -- Data da compra
    InvoiceDate AS invoice_date,

    -- Preço unitário
    UnitPrice AS unit_price,

    -- ID do cliente (pode estar nulo)
    CustomerID AS customer_id,

    -- País
    Country AS country,

    -- Valor total da linha
    Quantity * UnitPrice AS total_price

FROM retail_raw;