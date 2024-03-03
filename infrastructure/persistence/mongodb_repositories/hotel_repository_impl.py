from domain.repositories.hotel_repository import HotelRepository
from domain.models.hotel import Hotel
from mongodb_config import hotels_collection

class HotelRepositoryImpl(HotelRepository):
    def __init__(self):
        self.collection = hotels_collection

    def find_by_id(self, id: str) -> Hotel:
        hotel_data = self.collection.find_one({"_id": id})
        return Hotel(**hotel_data) if hotel_data else None
    
    def find_by_location_and_room_count(self, location: str, room_count: int):
        hotels_data = self.collection.find({"location": location, "rooms": {"$size": room_count}})
        return [Hotel(**hotel_data) for hotel_data in hotels_data]
