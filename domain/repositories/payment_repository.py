from abc import ABC, abstractmethod
from domain.models.payment import Payment

class PaymentRepository(ABC):
    @abstractmethod
    def save(self, payment: Payment):
        pass

    @abstractmethod
    def find_by_reservation_id(self, reservation_id: str) -> Payment:
        pass
