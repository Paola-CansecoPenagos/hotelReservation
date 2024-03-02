class Review:
    def __init__(self, id: str, hotel_id: str, user_id: str, rating: int, comment: str):
        self.id = id
        self.hotel_id = hotel_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
