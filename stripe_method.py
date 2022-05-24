import os

import stripe

SELLER_STRIPE_KEY = os.environ.get("SELLER_STRIPE_KEY")


class StripeSolution:
    def __init__(self, data):
        self.amount = data["amount"]
        self.currency = data["currency"]
        self.sender = data["sender"]
        self.receiver = data["receiver"]
        self.customer_api_key = data["customer_api_key"]

    def issue_payment(self):
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
