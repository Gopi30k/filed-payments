import re
import datetime
from .errors import InvalidCreditCard


class CreditCard():
    """[Acquiring Credit Card details and validating]
    """

    def __init__(self, CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode=None):
        # breakpoint()
        self.creditCardNumber = CreditCardNumber
        self.cardHolder = CardHolder
        self.expirationDate = ExpirationDate
        self.securityCode = SecurityCode
        self.amount = Amount

    def validate_card_number(self, no: str):
        """Validate Card Number

        Args:
            no ([str]): [description]

        Returns:
            [boolean]: [valid:False, Invalid: True]
        """
        return not(bool(re.match(r'^[456][0-9]{12}(?:[0-9]{3})?$', no)))

    # Getter and Setter for CreditCardNumber
    @property
    def creditCardNumber(self):
        return self._creditCardNumber

    @creditCardNumber.setter
    def creditCardNumber(self, cdNo):
        if not(isinstance(cdNo, str)) or self.validate_card_number(cdNo):
            errMsg = """CreditCard Number '{cardNumber}' is Invalid""".format(
                cardNumber=cdNo)
            raise InvalidCreditCard(errMsg)
        else:
            self._creditCardNumber = cdNo

    # Getter and Setter for CardHolder

    @property
    def cardHolder(self):
        return self._cardHolder

    @cardHolder.setter
    def cardHolder(self, name):
        if not(name):
            raise InvalidCreditCard("CardHolder Name is mandatory")
        elif not(isinstance(name, str)):
            raise InvalidCreditCard("CardHolder Name is not a String")
        else:
            self._cardHolder = name

    # Getter and Setter for ExpirationDate
    @property
    def expirationDate(self):
        return self._expirationDate

    @expirationDate.setter
    def expirationDate(self, expDate):
        if not(expDate):
            raise InvalidCreditCard("ExpirationDate is mandatory")
        elif not(bool(re.match(r'(\d{2}\/\d{4})$', expDate))) or datetime.datetime.strptime(expDate, "%m/%Y") < datetime.datetime.now():
            raise InvalidCreditCard("Invalid Expiration Date")
        else:
            self._expirationDate = expDate

    # Getter and Setter for Amount
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amt):
        if not(amt):
            raise InvalidCreditCard("Amount is mandatory")
        if not(isinstance(amt, float)) or amt < 0:
            raise InvalidCreditCard("Invalid Amount")
        else:
            self._amount = amt

    # Getter and Setter for SecurityCode
    @property
    def securityCode(self):
        return self._securityCode

    @securityCode.setter
    def securityCode(self, sCode):
        if sCode is not None and (not(isinstance(sCode, str)) or len(sCode) != 3):
            raise InvalidCreditCard("Invalid Security Code")
        else:
            self._securityCode = sCode

    # def __str__(self):
    #     return " Card Details :\n CreditCardNumber {cardNo} \n CardHolderName {name} \n ExpirationDate {expDate} \n Amount {amt} \n".format(cardNo=self._creditCardNumber, name=self._cardHolder, expDate=self._expirationDate, amt=self._amount)

    def __repr__(self):
        return """CreditCard(CreditCardNumber={cardNo}, CardHolder={name}, ExpirationDate={expDate}, Amount={amt})""".format(cardNo=self._creditCardNumber, name=self._cardHolder, expDate=self._expirationDate, amt=self._amount)
