SELECT
    country,
    ROUND(SUM(total_price), 2) AS revenue
FROM retail_final
GROUP BY country
ORDER BY revenue DESC;