-- Question:
-- Which customers have spent the most?

SELECT
    c.customer_name,
    c.city,
    COUNT(DISTINCT o.order_id) AS number_of_orders,
    ROUND(SUM(oi.quantity * p.price), 2) AS total_spent
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
JOIN order_items AS oi
    ON o.order_id = oi.order_id
JOIN products AS p
    ON oi.product_id = p.product_id
GROUP BY
    c.customer_id,
    c.customer_name,
    c.city
ORDER BY total_spent DESC;