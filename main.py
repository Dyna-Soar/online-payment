import os

import stripe

import paypalrestsdk


SELLER_STRIPE_KEY = os.environ.get("SELLER_STRIPE_KEY")

SELLER_PAYPAL_ID = os.environ.get("SELLER_PAYPAL_ID")
SELLER_PAYPAL_KEY = os.environ.get("SELLER_PAYPAL_KEY")


class PaymentGateway:
    def __init__(self, method, data):
        if method == "paypal":
            PaypalSolution(data)

        elif method == "stripe":
            StripeSolution(data)

"""
class PaymentSolution:
    def __init__(self, method, data):
        self.method = method
        self.data = data
        self.choose_solution()

    def choose_solution(self):
        if self.method == "paypal":
            PaypalSolution(self.data)

        elif self.method == "stripe":
            StripeSolution(self.data)
"""


class PaypalSolution:
    def __init__(self, data):
        self.amount = data["amount"]
        self.currency = data["currency"]
        self.sender = data["sender"]
        self.receiver = data["receiver"]

    def send_order(self):
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


class StripeSolution:
    def __init__(self, data):
        self.amount = data["amount"]
        self.currency = data["currency"]
        self.sender = data["sender"]
        self.receiver = data["receiver"]
        self.customer_api_key = data["customer_api_key"]

    def send_order(self):
        stripe.api_key = SELLER_STRIPE_KEY
        try:
            charge = stripe.Charge.create(
                amount=self.amount,
                currency=self.currency,
                description="Customer buy an item",
                source=self.customer_api_key,
            )
        except:
            raise ValueError("Missing or illegal value in data")
