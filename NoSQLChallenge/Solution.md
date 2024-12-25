# NoSQL Challenge Solution

### 1. Find all products in the "Electronics" category that have more than 50 items in stock:

```javascript
db.products.find({
  category: "Electronics",
  stock_quantity: {$gt: 50},
});
```

### 2. Find the total number of orders and total amount spent by a user (given their `user_id`):

```javascript
db.orders.aggregate([
    { $match: { user_id: <USER_ID> } }, // Match orders for the specific user_id
    {
        $group: {
            _id: "$user_id",
            totalOrders: { $sum: 1 }, 
            totalAmount: { $sum: "$total_amount" } 
        }
    }
]);
```

### 3. List all users who purchased a specific product (given its `product_id`):

```javascript
db.orders.aggregate([
    { $match: { product_ids: <PRODUCT_ID> } }, 
    {
        $lookup: {
            from: "users",
            localField: "user_id",
            foreignField: "user_id",
            as: "user_info"
        }
    },
    {
        $project: {
            "user_info.name": 1,
            "user_info.email": 1,
            _id: 0
                    }
    }
]);
```

### 4. Update stock quantity of a product (given its `product_id` and purchased quantity):

```javascript
db.products.updateOne(
    { product_id: <PRODUCT_ID> }, 
    { $inc: { stock_quantity: -<PURCHASED_QUANTITY> } }
```
