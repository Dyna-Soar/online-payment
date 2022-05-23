import stripe


class PaymentSolution:
    def __init__(self, method, data):
        self.method = method
        self.data = data
        self.choose_solution()

    def choose_solution(self):
        if self.data["method"] == "paypal":
            PaypalSolution(self.data)

        elif self.data["method"] == "stripe":
            StripeSolution(self.data)


class PaypalSolution:
    def __init__(self, data):
        self.amount = data["amount"]
        self.sender = data["sender"]
        self.receiver = data["receiver"]


class StripeSolution:
    def __init__(self, data):
        self.amount = data["amount"]
        self.sender = data["sender"]
        self.receiver = data["receiver"]
