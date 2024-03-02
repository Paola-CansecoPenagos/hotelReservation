from domain.repositories.hotel_repository import HotelRepository
from domain.models.hotel import Hotel
from mongodb_config import hotels_collection

class HotelRepositoryImpl(HotelRepository):
    def __init__(self):
        self.collection = hotels_collection

    def find_by_id(self, id: str) -> Hotel:
        hotel_data = self.collection.find_one({"_id": id})
        return Hotel(**hotel_data) if hotel_data else None
