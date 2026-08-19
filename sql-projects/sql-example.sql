-- SQL Portfolio Example
-- A small SQLite-style example showing import, inspection, filtering,
-- grouping, sorting, and joining.

-- CHUNK 1: Create a small customer table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    state TEXT,
    income REAL
);

INSERT INTO customers VALUES
(1, 'Asha', 'TX', 62000),
(2, 'Brian', 'GA', 54000),
(3, 'Carlos', 'TX', 71000),
(4, 'Diana', 'CA', 88000),
(5, 'Elena', 'GA', 59000);

-- CHUNK 2: Create a purchase table
CREATE TABLE purchases (
    purchase_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    category TEXT,
    amount REAL
);

INSERT INTO purchases VALUES
(101, 1, 'Data', 120),
(102, 1, 'Books', 85),
(103, 2, 'Data', 150),
(104, 3, 'Software', 240),
(105, 3, 'Books', 60),
(106, 4, 'Software', 310),
(107, 5, 'Data', 95);

-- CHUNK 3: Inspect the dataset
SELECT *
FROM customers;

-- CHUNK 4: Filter observations
SELECT customer_name, state, income
FROM customers
WHERE income >= 60000
ORDER BY income DESC;

-- CHUNK 5: Summarize purchases by category
SELECT category,
       COUNT(*) AS purchases,
       ROUND(SUM(amount), 2) AS total_spending,
       ROUND(AVG(amount), 2) AS average_spending
FROM purchases
GROUP BY category
ORDER BY total_spending DESC;

-- CHUNK 6: Join customer and purchase information
SELECT c.customer_name,
       c.state,
       p.category,
       p.amount
FROM customers AS c
JOIN purchases AS p
  ON c.customer_id = p.customer_id
ORDER BY p.amount DESC;

-- CHUNK 7: Find customers whose total spending exceeds $150
SELECT c.customer_name,
       ROUND(SUM(p.amount), 2) AS total_spending
FROM customers AS c
JOIN purchases AS p
  ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) > 150
ORDER BY total_spending DESC;
