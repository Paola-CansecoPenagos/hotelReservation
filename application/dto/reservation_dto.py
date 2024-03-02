class ReservationDTO:
    def __init__(self, user_id: str, hotel_id: str, room_id: str, start_date, end_date):
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.room_id = room_id
        self.start_date = start_date
        self.end_date = end_date
