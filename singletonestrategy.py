class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Purchasing {amount} by Credit Card")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Purchasing {amount} by PayPal")

class PaymentProcess:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PaymentProcess, cls).__new__(cls)
            cls._instance.strategy = None
        return cls._instance

    def payment_strategy(self, strategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        if not self.strategy:
            raise ValueError("Payment strategy not set")
        self.strategy.pay(amount)
if __name__ == "__main__":
    context1 = PaymentProcess()
    context2 = PaymentProcess()
    print(context1 is context2)

    credit_card_strategy = CreditCard()
    paypal_strategy = PayPal()

    context = PaymentProcess()

    context.payment_strategy(credit_card_strategy)
    context.execute_payment(100)

    context.payment_strategy(paypal_strategy)
    context.execute_payment(50)