from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, transaction_id):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

    def refund(self, transaction_id):
        return f"Refunding credit card transaction {transaction_id}"


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

    def refund(self, transaction_id):
        return f"Refunding PayPal transaction {transaction_id}"


class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"

    def refund(self, transaction_id):
        return f"Refunding Stripe transaction {transaction_id}"


class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Cryptocurrency"

    def refund(self, transaction_id):
        return f"Refunding crypto transaction {transaction_id}"


class PaymentFactory:
    def __init__(self):
        self._processors = {}

    def register_processor(self, payment_type, processor_class):
        self._processors[payment_type] = processor_class

    def create_processor(self, payment_type):
        processor_class = self._processors.get(payment_type)
        if processor_class:
            return processor_class()
        raise ValueError(f"Payment type {payment_type} not registered")


# Usage
factory = PaymentFactory()
factory.register_processor('credit_card', CreditCardProcessor)
factory.register_processor('paypal', PayPalProcessor)
factory.register_processor('stripe', StripeProcessor)

processor = factory.create_processor('stripe')
print(processor.process_payment(99.99))

processor = factory.create_processor('stripe')
print(processor.process_payment(20.87))
