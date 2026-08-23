-- Question:
-- How do sales change over time?

SELECT
    strftime('%Y-%m', o.order_date) AS month,
    COUNT(DISTINCT o.order_id) AS number_of_orders,
    ROUND(SUM(oi.quantity * p.price), 2) AS revenue
FROM orders AS o
JOIN order_items AS oi
    ON o.order_id = oi.order_id
JOIN products AS p
    ON oi.product_id = p.product_id
GROUP BY month
ORDER BY month;