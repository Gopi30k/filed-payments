import unittest
import requests
import json


class FiledPaymentTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/process-payment"

    def test_payment_for_invalid_request(self):
        """Sending an empty request for payment
        """
        testResponse = requests.post(FiledPaymentTest.API_URL, json={})
        self.assertEqual(testResponse.status_code, 500)
        self.assertDictEqual(testResponse.json(), {
            "msg": "Invalid Request"
        })

    def test_payment_for_invalid_CreditCardNumber(self):
        """ CreditCardNumber (mandatory, string, it should be a valid credit card number)
            Issue created - Length exceeded and letter in number
        """

        testResponse_1 = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "33245234k776723",
            "CardHolder": "Gopi Krishnan",
            "SecurityCode": "111",
            "ExpirationDate": "12/2022",
            "Amount": 66.34
        })

        self.assertEqual(testResponse_1.status_code, 400)
        self.assertDictEqual(testResponse_1.json(), {
            "msg": "CreditCard Number '33245234k776723' is Invalid"
        })

    def test_payment_for_invalid_Cardholder(self):
        """ Cardholder Name (mandatory, string)
            Issue created - Number instead of string as name
        """
        #
        testResponse_2 = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "4123456789123",
            "CardHolder": 3435,
            "SecurityCode": "111",
            "ExpirationDate": "12/2022",
            "Amount": 66.34
        })

        self.assertEqual(testResponse_2.status_code, 400)
        self.assertDictEqual(testResponse_2.json(), {
            "msg": "CardHolder Name is not a String"
        })

    def test_payment_for_invalid_SecurityCode(self):
        """ 
            Wrong Security Code - SecurityCode (optional, string, 3 digits)
            Issue created - 4 digit security code
        """
        #
        testResponse_3 = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "4123456789123",
            "CardHolder": "Gopi Krishnan",
            "SecurityCode": "1211",
            "ExpirationDate": "12/2022",
            "Amount": 66.34
        })

        self.assertEqual(testResponse_3.status_code, 400)
        self.assertDictEqual(testResponse_3.json(), {
            "msg": "Invalid Security Code"
        })

    def test_payment_for_invalid_ExpirationDate(self):
        """ 
            ExpirationDate (mandatory, DateTime, it cannot be in the past)
            Issue created - Date is given in past
        """
        testResponse_4 = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "4123456789123",
            "CardHolder": "Gopi Krishnan",
            "SecurityCode": "111",
            "ExpirationDate": "12/2020",
            "Amount": 66.34
        })

        self.assertEqual(testResponse_4.status_code, 400)
        self.assertDictEqual(testResponse_4.json(), {
            "msg": "Invalid Expiration Date"
        })

    def test_payment_for_invalid_Amount(self):
        """ 
            Amount (mandatoy decimal, positive amount)
            Issue created - Amount is in Number
        """

        testResponse_5 = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "4123456789123",
            "CardHolder": "Gopi Krishnan",
            "SecurityCode": "111",
            "ExpirationDate": "12/2022",
            "Amount": 664
        })

        self.assertEqual(testResponse_5.status_code, 400)
        self.assertDictEqual(testResponse_5.json(), {
            "msg": "Invalid Amount"
        })

    def test_process_payment_via_CheapPaymentGateway(self):
        """
            - If the amount to be paid is less than £20, use CheapPaymentGateway.
        """
        testResponse = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "4123456789123",
            "CardHolder": "Gopi Krishnan",
            "SecurityCode": "111",
            "ExpirationDate": "12/2022",
            "Amount": 12.00
        })

        self.assertEqual(testResponse.status_code, 200)
        self.assertDictEqual(testResponse.json(), {
            "msg": "Payment Successfull of £12.0 view CheapPaymentGateway"
        })

    def test_process_payment_via_ExpensivePaymentGateway(self):
        """
            - If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
            Otherwise, retry only once with CheapPaymentGateway
        """
        testResponse = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "4123456789123",
            "CardHolder": "Gopi Krishnan",
            "SecurityCode": "111",
            "ExpirationDate": "02/2021",
            "Amount": 412.46
        })

        self.assertEqual(testResponse.status_code, 200)
        self.assertDictEqual(testResponse.json(), {
            "msg": "Payment Successfull of £412.46 view ExpensivePaymentGateway"
        })

    def test_process_payment_via_ExpensivePaymentGateway(self):
        """
            - If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
            Otherwise, retry only once with CheapPaymentGateway
        """
        testResponse = requests.post(FiledPaymentTest.API_URL, json={
            "CreditCardNumber": "3455689021874289",
            "CardHolder": "Gopi Krishnan",
            "SecurityCode": "111",
            "ExpirationDate": "06/2021",
            "Amount": 999.12
        })

        self.assertEqual(testResponse.status_code, 200)
        self.assertDictEqual(testResponse.json(), {
            "msg": "Payment Successfull of £999.12 view PremiumPaymentGateway"
        })
