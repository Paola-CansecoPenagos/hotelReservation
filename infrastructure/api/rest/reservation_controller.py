from flask import Blueprint, jsonify, request
from domain.services.reservation_service import ReservationService
from application.dto.reservation_dto import ReservationDTO
from application.use_cases.create_reservation import CreateReservationUseCase

reservation_blueprint = Blueprint('reservation', __name__)
reservation_service = ReservationService()

@reservation_blueprint.route('/<reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = reservation_service.find_by_id(reservation_id)
    if reservation:
        return jsonify(reservation.to_dict()), 200
    else:
        return jsonify({"message": "Reservation not found"}), 404

@reservation_blueprint.route('/<reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    data = request.json
    updated_reservation = reservation_service.update_reservation(reservation_id, data)
    if updated_reservation:
        return jsonify(updated_reservation.to_dict()), 200
    else:
        return jsonify({"message": "Failed to update reservation"}), 400

@reservation_blueprint.route('/<reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    result = reservation_service.cancel_reservation(reservation_id)
    if result:
        return jsonify({"message": "Reservation cancelled successfully"}), 200
    else:
        return jsonify({"message": "Failed to cancel reservation"}), 400

@reservation_blueprint.route('/user/<user_id>', methods=['GET'])
def get_user_reservations(user_id):
    reservations = reservation_service.find_by_user_id(user_id)
    if reservations:
        return jsonify([reservation.to_dict() for reservation in reservations]), 200
    else:
        return jsonify({"message": "No reservations found for this user"}), 404

@reservation_blueprint.route('/api/reservations', methods=['POST'])
def create_reservation():
    reservation_service = ReservationService()
    create_reservation_use_case = CreateReservationUseCase(reservation_service)

    data = request.json
    reservation_dto = ReservationDTO(
        user_id=data['user_id'],
        hotel_id=data['hotel_id'],
        room_id=data['room_id'],
        start_date=data['start_date'],
        end_date=data['end_date']
    )

    created_reservation = create_reservation_use_case.execute(reservation_dto)
    return jsonify({"message": "Reservation created successfully"}), 201