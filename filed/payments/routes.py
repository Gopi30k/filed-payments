from flask import Blueprint, request
from flask.json import jsonify
from .utils import CreditCard
from .errors import InvalidCreditCard
from .gateway import CheapPaymentGateway, PaymentGateway
import json
payment = Blueprint('users', __name__)


@payment.route("/", methods=["GET"])
def index():
    return "Hello Filed.com"


@payment.route("/credit-card", methods=["POST"])
def processPayment():
    try:
        request_data = request.json
        card = CreditCard(**request_data)

        if card.amount < 20:
            payment_gateway = CheapPaymentGateway(card)
            print(payment_gateway.authorize())
        return jsonify(msg="Credentials Authenticated"), 200
    except InvalidCreditCard as err:
        return jsonify(msg=str(err)), 400
    except Exception as e:
        return jsonify(msg="Invalid Request"), 400
