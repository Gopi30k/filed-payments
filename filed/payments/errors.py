class InvalidCreditCard(Exception):
    def __init__(self,  message):
        self.message = message
        super(InvalidCreditCard, self).__init__(self.message)

    def __str__(self):
        return self.message
