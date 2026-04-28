SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN order_count = 1 THEN 1 ELSE 0 END) AS one_time_customers,
    SUM(CASE WHEN order_count > 1 THEN 1 ELSE 0 END) AS repeat_customers
FROM (
    SELECT
        customer_id,
        COUNT(DISTINCT invoice_no) AS order_count
    FROM retail_final
    GROUP BY customer_id
);