from paypal_method import PaypalSolution
from stripe_method import StripeSolution


class PaymentGateway:
    def __init__(self, method, data):
        if method == "paypal":
            PaypalSolution(data)

        elif method == "stripe":
            StripeSolution(data)

