-- Receita total
SELECT
    ROUND(SUM(total_price), 2) AS total_revenue
FROM retail_final;

-- Ticket médio por pedido
SELECT
    ROUND(AVG(order_total), 2) AS avg_ticket
FROM (
    SELECT
        invoice_no,
        SUM(total_price) AS order_total
    FROM retail_final
    GROUP BY invoice_no
);