from flask import Blueprint

payment = Blueprint('users', __name__)


@payment.route("/", methods=["GET"])
def index():
    return "Hello Filed.com"
