from flask import Blueprint, jsonify, request
from domain.services.hotel_service import HotelService
from infrastructure.persistence.mongodb_repositories.hotel_repository_impl import HotelRepositoryImpl

hotel_blueprint = Blueprint('hotel', __name__)
hotel_repository = HotelRepositoryImpl()  # Asumiendo que tienes una implementación concreta de HotelRepository
hotel_service = HotelService(hotel_repository)  # Crear una instancia de HotelService pasando hotel_repository

@hotel_blueprint.route('/<hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotel = hotel_service.find_by_id(hotel_id)
    if hotel:
        return jsonify(hotel.to_dict()), 200
    else:
        return jsonify({"message": "Hotel not found"}), 404
