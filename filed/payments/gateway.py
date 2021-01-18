from .utils import CreditCard


class PaymentGateway():
    def __init__(self, cardDetails):
        self.cardDetails = cardDetails

    def authorize(self):
        return isinstance(self.cardDetails, CreditCard)

    def pay(self):
        pass


class CheapPaymentGateway(PaymentGateway):
    def __init__(self, cardDetails):
        super().__init__(cardDetails)

    def pay(self):
        pass
