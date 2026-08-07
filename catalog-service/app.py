from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1000
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 100
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 50
    }
]


@app.route("/")
def home():
    return "Catalog Service Running"


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "catalog"
    })


@app.route("/products")
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>")
def get_product(product_id):

    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({
        "error": "Product not found"
    }), 404



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5050
    )