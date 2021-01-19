class InvalidCreditCard(Exception):
    """Custom Exception Handeler for Invalid Credit Card Details
    """
    def __init__(self,  message):
        self.message = message
        super(InvalidCreditCard, self).__init__(self.message)

    def __str__(self):
        return self.message
