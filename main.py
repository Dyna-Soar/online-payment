import gateway


if __name__ == "__main__":
    gateway.PaymentGateway(input("method: "), input("data: "))
else:
    def send_to_gateway(method, data):
        gateway.PaymentGateway(method, data)
