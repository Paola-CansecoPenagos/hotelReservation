from flask import Blueprint, jsonify, request
from domain.services.hotel_service import HotelService

hotel_blueprint = Blueprint('hotel', __name__)

@hotel_blueprint.route('/<hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotel = HotelService.find_by_id(hotel_id)
    if hotel:
        return jsonify(hotel.to_dict()), 200
    else:
        return jsonify({"message": "Hotel not found"}), 404
