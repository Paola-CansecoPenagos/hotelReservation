from datetime import datetime

class Payment:
    def __init__(self, id: str, reservation_id: str, amount: float, date: datetime):
        self.id = id
        self.reservation_id = reservation_id
        self.amount = amount
        self.date = date
