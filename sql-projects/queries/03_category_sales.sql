-- Question:
-- Which product categories generate the most revenue?

SELECT
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.quantity * p.price), 2) AS revenue
FROM order_items AS oi
JOIN products AS p
    ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;