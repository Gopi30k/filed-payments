"""
    Author: Gopi Krishnan
    Description: This Module holds URL routing related to payment processing
"""


from flask import Blueprint, request, session
from flask.json import jsonify
from .utils import CreditCard
from .errors import InvalidCreditCard
from .gateway import CheapPaymentGateway, ExpensivePaymentGateway, PremiumPaymentGateway
import json
payment = Blueprint('users', __name__)


@payment.route("/", methods=["GET"])
def index():
    """ Welcome API
    """
    return "Hello Filed.com"


@payment.route("/process-payment", methods=["POST"])
def processPayment():
    """ Process payment Request

    Returns:
        JSON Response: returns status code and message
    """
    try:
        request_data = request.json
        card = CreditCard(**request_data)
        payment_status = ''
        payment_type = None
        if card.amount <= 20:
            payment_type = CheapPaymentGateway(card)
        elif 20 < card.amount < 500:
            payment_type = ExpensivePaymentGateway(card)
        elif card.amount >= 500:
            payment_type = PremiumPaymentGateway(card)
        if payment_type.authorize():
            payment_status = payment_type.pay(card.amount)
        return jsonify(msg=payment_status), 200
    except InvalidCreditCard as err:
        return jsonify(msg=str(err)), 400
    except Exception:
        return jsonify(msg="Invalid Request"), 500
