from abc import ABC, abstractmethod

class HotelRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str):
        pass

    @abstractmethod
    def find_by_location_and_room_count(self, location: str, room_count: int):
        pass