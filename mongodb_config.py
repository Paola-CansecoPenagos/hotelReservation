from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017/')
database = mongo_client['hotelReservations']

hotels_collection = database['hotels']
users_collection = database['users']
