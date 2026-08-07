from flask import Flask, jsonify
import requests
import os


app = Flask(__name__)


orders = []



CART_SERVICE = os.getenv(
    "CART_SERVICE",
    "http://localhost:5001"
)


PAYMENT_SERVICE = os.getenv(
    "PAYMENT_SERVICE",
    "http://localhost:5002"
)




@app.route("/")
def home():

    return "Order Service Running"



@app.route("/health")
def health():

    return jsonify({

        "status":"UP",

        "service":"order"

    })




@app.route("/orders", methods=["POST"])
def create_order():


    cart_response = requests.get(

        f"{CART_SERVICE}/cart"

    )


    cart_items = cart_response.json()



    if len(cart_items)==0:

        return jsonify({

            "error":"Cart is empty"

        }),400



    total = 0



    for item in cart_items:

        total += item["price"] * item["quantity"]




    payment_response = requests.post(

        f"{PAYMENT_SERVICE}/payment",

        json={

            "amount":total

        }

    )



    payment = payment_response.json()



    if payment["status"]!="SUCCESS":

        return jsonify({

            "message":"Payment failed",

            "payment":payment

        }),400





    order = {


        "order_id":len(orders)+1,


        "items":cart_items,


        "total":total,


        "payment":payment,


        "status":"CONFIRMED"


    }




    orders.append(order)



    return jsonify(order),201




@app.route("/orders")
def get_orders():

    return jsonify(orders)





if __name__=="__main__":


    app.run(

        host="0.0.0.0",

        port=5003

    )