import os

import stripe


SELLER_STRIPE_KEY = os.environ.get("SELLER_STRIPE_KEY")

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


class StripeSolution:
    def __init__(self, data):
        self.amount = data["amount"]
        self.currency = data["currency"]
        self.sender = data["sender"]
        self.receiver = data["receiver"]
        self.api_key = data["api_key"]

    def send_order(self):
        stripe.api_key = self.api_key
        try:
            charge = stripe.Charge.create(
                amount=self.amount,
                currency=self.currency,
                description="Customer buy an item",
                source=SELLER_STRIPE_KEY,
                idempotency_key=''
            )
        except:
            raise ValueError("Missing or illegal value in data")
