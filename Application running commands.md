Take any terminal

See the products:

curl http://localhost:5050/products


Adding products in cart:

curl -X POST http://localhost:5001/cart \
-H "Content-Type: application/json" \
-d '{
    "product_id":1,
    "quantity":2
}'

Create a order and Payment:

curl -X POST http://localhost:5003/orders