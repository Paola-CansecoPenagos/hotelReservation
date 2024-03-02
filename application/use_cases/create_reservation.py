from application.dto.reservation_dto import ReservationDTO
from domain.models.reservation import Reservation
from domain.services.reservation_service import ReservationService

class CreateReservationUseCase:
    def __init__(self, reservation_service: ReservationService):
        self.reservation_service = reservation_service

    def execute(self, reservation_dto: ReservationDTO):
        reservation = Reservation(
            id=None,
            user_id=reservation_dto.user_id,
            hotel_id=reservation_dto.hotel_id,
            room_id=reservation_dto.room_id,
            start_date=reservation_dto.start_date,
            end_date=reservation_dto.end_date
        )

        created_reservation = self.reservation_service.create_reservation(reservation)
        
        return created_reservation
