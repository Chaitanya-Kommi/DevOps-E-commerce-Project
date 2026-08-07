from flask import Flask, jsonify, request
import uuid
from datetime import datetime


app = Flask(__name__)


payments = []



@app.route("/")
def home():

    return "Payment Service Running"



@app.route("/health")
def health():

    return jsonify({

        "status":"UP",

        "service":"payment"

    })



@app.route("/payment", methods=["POST"])
def make_payment():


    data = request.json


    amount = data["amount"]



    if amount <= 0:

        return jsonify({

            "status":"FAILED",

            "reason":"Invalid amount"

        }),400



    if amount > 5000:

        payment = {

            "payment_id":len(payments)+1,

            "transaction_id":str(uuid.uuid4()),

            "amount":amount,

            "status":"FAILED",

            "reason":"Transaction declined"

        }


        payments.append(payment)


        return jsonify(payment),402



    payment = {


        "payment_id":len(payments)+1,


        "transaction_id":str(uuid.uuid4()),


        "amount":amount,


        "status":"SUCCESS",


        "created_at":datetime.now().isoformat()

    }


    payments.append(payment)


    return jsonify(payment),201




@app.route("/payments")
def get_payments():

    return jsonify(payments)




if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5002
    )