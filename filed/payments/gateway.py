from .utils import CreditCard


class PaymentGateway():
    """ Basic Payment Gateway to manage underlaying process
    """

    def __init__(self, cardDetails):
        self.cardDetails = cardDetails

    def authorize(self):
        """Dummy Authoriazation mechanism to check whether a valid credit card is accessing the Gateway

        Returns:
            [Boolean]: [Gateway is authorized or not]
        """
        return isinstance(self.cardDetails, CreditCard)

    def pay(self, amount):
        pass


class CheapPaymentGateway(PaymentGateway):
    def __init__(self, cardDetails):
        super().__init__(cardDetails)

    def pay(self, amount):
        return "Payment Successfull of £{amt} view CheapPaymentGateway".format(amt=amount)


class ExpensivePaymentGateway(PaymentGateway):
    def __init__(self, cardDetails):
        super().__init__(cardDetails)

    def pay(self, amount):
        return "Payment Successfull of £{amt} view ExpensivePaymentGateway".format(amt=amount)


class PremiumPaymentGateway(PaymentGateway):
    def __init__(self, cardDetails):
        super().__init__(cardDetails)

    def pay(self, amount):
        return "Payment Successfull of £{amt} view PremiumPaymentGateway".format(amt=amount)
