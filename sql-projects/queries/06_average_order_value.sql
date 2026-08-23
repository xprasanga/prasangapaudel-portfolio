-- Question:
-- What is the average value of an order?

SELECT
    ROUND(AVG(order_total), 2) AS average_order_value
FROM (
    SELECT
        o.order_id,
        SUM(oi.quantity * p.price) AS order_total
    FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_id
    JOIN products AS p
        ON oi.product_id = p.product_id
    GROUP BY o.order_id
);