from domain.repositories.hotel_repository import HotelRepository

class HotelService:
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def find_by_id(self, hotel_id: str):
        return self.hotel_repository.find_by_id(hotel_id)
    
    def find_by_location_and_room_count(self, location: str, room_count: int):
        return self.hotel_repository.find_by_location_and_room_count(location, room_count)