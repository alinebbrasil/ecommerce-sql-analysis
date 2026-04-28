SELECT
    customer_id,
    ROUND(SUM(total_price), 2) AS total_spent,
    COUNT(DISTINCT invoice_no) AS total_orders,
    ROUND(SUM(total_price) / COUNT(DISTINCT invoice_no), 2) AS avg_order_value
FROM retail_final
GROUP BY customer_id
ORDER BY total_spent DESC;