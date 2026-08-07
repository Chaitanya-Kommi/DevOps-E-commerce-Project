from flask import Flask, jsonify, request
import requests
import os


app = Flask(__name__)

cart = []


CATALOG_SERVICE = os.getenv(
    "CATALOG_SERVICE",
    "http://localhost:5050"
)


@app.route("/")
def home():
    return "Cart Service Running"


@app.route("/health")
def health():

    return jsonify({
        "status":"UP",
        "service":"cart"
    })


@app.route("/cart", methods=["GET"])
def get_cart():

    return jsonify(cart)



@app.route("/cart", methods=["POST"])
def add_to_cart():

    data = request.json


    product_id = data["product_id"]

    quantity = data["quantity"]


    response = requests.get(
        f"{CATALOG_SERVICE}/products/{product_id}"
    )


    if response.status_code != 200:

        return jsonify({
            "error":"Product not found"
        }),404



    product = response.json()



    cart_item = {

        "id": product["id"],

        "name": product["name"],

        "price": product["price"],

        "quantity": quantity
    }


    cart.append(cart_item)


    return jsonify({

        "message":"Item added successfully",

        "cart":cart

    }),201



@app.route("/cart/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):

    global cart


    cart = [

        item for item in cart

        if item["id"] != item_id

    ]


    return jsonify({

        "message":"Item removed",

        "cart":cart

    })



if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5001
    )