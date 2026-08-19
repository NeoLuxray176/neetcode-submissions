-- Write your query below
SELECT name
FROM customers
WHERE id NOT in (SELECT customer_id FROM orders);