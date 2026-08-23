-- ============================================================
-- Dummy Retail Sales Data
-- ============================================================

INSERT INTO customers
    (customer_id, customer_name, city, signup_date)
VALUES
    (1, 'Alice Johnson', 'Austin', '2024-01-15'),
    (2, 'Brian Smith', 'Dallas', '2024-02-20'),
    (3, 'Carlos Garcia', 'Houston', '2024-03-10'),
    (4, 'Diana Brown', 'Austin', '2024-04-05'),
    (5, 'Emily Davis', 'Dallas', '2024-05-18'),
    (6, 'Frank Wilson', 'Houston', '2024-06-22'),
    (7, 'Grace Miller', 'Austin', '2024-07-11'),
    (8, 'Henry Moore', 'Dallas', '2024-08-30');

INSERT INTO products
    (product_id, product_name, category, price)
VALUES
    (101, 'Laptop', 'Electronics', 899.99),
    (102, 'Wireless Mouse', 'Electronics', 29.99),
    (103, 'Keyboard', 'Electronics', 59.99),
    (104, 'Coffee Maker', 'Home', 79.99),
    (105, 'Desk Lamp', 'Home', 34.99),
    (106, 'Office Chair', 'Furniture', 249.99),
    (107, 'Desk', 'Furniture', 399.99),
    (108, 'Notebook', 'Office Supplies', 8.99);

INSERT INTO orders
    (order_id, customer_id, order_date)
VALUES
    (1001, 1, '2024-01-20'),
    (1002, 2, '2024-02-25'),
    (1003, 3, '2024-03-15'),
    (1004, 1, '2024-04-12'),
    (1005, 4, '2024-04-18'),
    (1006, 5, '2024-05-22'),
    (1007, 6, '2024-06-28'),
    (1008, 7, '2024-07-19'),
    (1009, 8, '2024-08-31'),
    (1010, 2, '2024-09-05'),
    (1011, 3, '2024-09-15'),
    (1012, 4, '2024-10-10');

INSERT INTO order_items
    (order_item_id, order_id, product_id, quantity)
VALUES
    (1, 1001, 101, 1),
    (2, 1001, 102, 2),

    (3, 1002, 104, 1),
    (4, 1002, 105, 2),

    (5, 1003, 106, 1),
    (6, 1003, 108, 5),

    (7, 1004, 103, 1),
    (8, 1004, 102, 1),

    (9, 1005, 107, 1),

    (10, 1006, 101, 1),
    (11, 1006, 103, 1),

    (12, 1007, 104, 2),
    (13, 1007, 108, 10),

    (14, 1008, 106, 1),
    (15, 1008, 105, 1),

    (16, 1009, 102, 3),
    (17, 1009, 103, 2),

    (18, 1010, 107, 1),
    (19, 1010, 108, 5),

    (20, 1011, 101, 1),
    (21, 1011, 102, 1),

    (22, 1012, 104, 1),
    (23, 1012, 105, 1);