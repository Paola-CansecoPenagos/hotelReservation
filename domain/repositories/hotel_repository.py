from abc import ABC, abstractmethod

class HotelRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str):
        pass
