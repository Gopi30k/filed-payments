from flask import Flask


def create_app():
    app = Flask(__name__)

    from filed.payments.routes import payment
    app.register_blueprint(payment)

    return app
