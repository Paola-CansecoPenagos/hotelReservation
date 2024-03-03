from flask import Blueprint, jsonify, request
from domain.services.hotel_service import HotelService
from infrastructure.persistence.mongodb_repositories.hotel_repository_impl import HotelRepositoryImpl

hotel_blueprint = Blueprint('hotel', __name__)
hotel_repository = HotelRepositoryImpl()  
hotel_service = HotelService(hotel_repository)  

@hotel_blueprint.route('/<hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotel = hotel_service.find_by_id(hotel_id)
    if hotel:
        return jsonify(hotel.to_dict()), 200
    else:
        return jsonify({"message": "Hotel not found"}), 404

@hotel_blueprint.route('/hotels', methods=['GET'])
def get_hotels_by_location_and_room_count():
    location = request.args.get('location')
    room_count_str = request.args.get('room_count')

    if room_count_str is not None:
        try:
            room_count = int(room_count_str)
        except ValueError:
            return jsonify({"message": "Invalid room count"}), 400
    else:
        room_count = None

    hotels = hotel_service.find_by_location_and_room_count(location, room_count)
    if hotels:
        return jsonify([hotel.to_dict() for hotel in hotels]), 200
    else:
        return jsonify({"message": "Hotels not found"}), 404