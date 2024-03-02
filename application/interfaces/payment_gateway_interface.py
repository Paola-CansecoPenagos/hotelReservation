from abc import ABC, abstractmethod

class PaymentGatewayInterface(ABC):
    @abstractmethod
    def process_payment(self, amount: float, payment_details: dict):
        pass
