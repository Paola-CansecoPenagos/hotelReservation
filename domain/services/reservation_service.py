class ReservationService:
    def __init__(self, reservation_repository, hotel_repository):
        self.reservation_repository = reservation_repository
        self.hotel_repository = hotel_repository

    def create_reservation(self, reservation):
        hotel = self.hotel_repository.find_by_id(reservation.hotel_id)
        if not hotel:
            raise ValueError("Hotel no encontrado")

        room_available = self._check_room_availability(reservation.hotel_id, reservation.room_id, reservation.start_date, reservation.end_date)
        if not room_available:
            raise ValueError("La habitación no está disponible para las fechas seleccionadas")

        new_reservation = self.reservation_repository.save(reservation)
        return new_reservation

    def _check_room_availability(self, hotel_id, room_id, start_date, end_date):
        existing_reservations = self.reservation_repository.find_by_room_id(room_id)

        for reservation in existing_reservations:
            if start_date < reservation.end_date and end_date > reservation.start_date:
                return False

        return True 

