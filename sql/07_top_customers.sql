SELECT
    customer_id,
    ROUND(SUM(total_price), 2) AS total_spent
FROM retail_final
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;