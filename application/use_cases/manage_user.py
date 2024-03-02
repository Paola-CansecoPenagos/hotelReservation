from application.dto.user_dto import UserDTO
from domain.models.user import User
from domain.repositories.user_repository import UserRepository

class ManageUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user_dto: UserDTO):
        user = User(
            id=None,  
            name=user_dto.name,
            email=user_dto.email,
            password=user_dto.password 
        )
        
        created_user = self.user_repository.save(user)
        return created_user

    def update_user_info(self, user_id, user_dto: UserDTO):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado")

        user.name = user_dto.name
        user.email = user_dto.email
        user.password = user_dto.password 

        updated_user = self.user_repository.update(user_id, user)
        return updated_user
