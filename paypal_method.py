"""
    TODO: pay with customer's credit card information
          As a customer i want to use my credit card, so i can buy the product
    TODO: pay with customer's paypal account
          As a customer i want to use my paypal account, so i can buy the product
"""

import os

import paypalrestsdk

SELLER_PAYPAL_ID = os.environ.get("SELLER_PAYPAL_ID")
SELLER_PAYPAL_KEY = os.environ.get("SELLER_PAYPAL_KEY")


class PaypalSolution:
    def __init__(self, data):
        self.amount = data["amount"]
        self.currency = data["currency"]
        self.sender = data["sender"]
        self.receiver = data["receiver"]

    def issue_payment(self):
        paypalrestsdk.configure({
            "mode": "sandbox",  # sandbox or live
            "client_id": SELLER_PAYPAL_ID,
            "client_secret": SELLER_PAYPAL_KEY})

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": self.amount,
                        "currency": self.currency,
                        "quantity": 1}]},
                "amount": {
                    "total": self.amount,
                    "currency": self.currency},
                "description": "This is the payment transaction description."}]})

        if payment.create():
            print("Payment created successfully")
        else:
            print(payment.error)
