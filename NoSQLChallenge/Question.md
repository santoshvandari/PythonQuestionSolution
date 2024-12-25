# NoSQL Challenge

You are given the following MongoDB collections for an online store:

- `products (product_id , name, category, price, stock_quantity)`
- `orders (order_id, user_id, product_ids, order_date, total_amount)`
- `users (user_id, name, email, address)`

Write the following MongoDB queries for the store:

1. Find all products in the "Electronics" category that have more than 50 items in stock.
2. Find the total number of orders placed by a user (given their user_id), including the total amount spent.
3. List all users who have purchased a specific product (given its product_id), including their name and email address.
4. Update the stock quantity of a product (given its product_id) after an order is placed, considering the quantity of the product purchased in the order.