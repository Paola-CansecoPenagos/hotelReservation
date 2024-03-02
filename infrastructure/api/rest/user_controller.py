from flask import Blueprint, request, jsonify
from application.use_cases.manage_user import ManageUserUseCase
from application.dto.user_dto import UserDTO
from infrastructure.persistence.mongodb_repositories.user_repository_impl import UserRepositoryImpl

user_blueprint = Blueprint('user', __name__)
user_repository = UserRepositoryImpl() 
manage_user_use_case = ManageUserUseCase(user_repository)

@user_blueprint.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user_dto = UserDTO(name=data['name'], email=data['email'], password=data['password'])
    
    result = manage_user_use_case.register_user(user_dto)
    
    if result:
        return jsonify({"message": "User registered successfully"}), 201
    else:
        return jsonify({"error": "Registration failed"}), 400
