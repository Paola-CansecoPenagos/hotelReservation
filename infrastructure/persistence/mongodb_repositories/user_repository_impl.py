from pymongo.collection import Collection
from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from mongodb_config import users_collection  

class UserRepositoryImpl(UserRepository):
    def __init__(self):
        self.collection = users_collection

    def save(self, user: User) -> User:
        user_data = user.__dict__
        result = self.collection.insert_one(user_data)
        user.id = result.inserted_id  
        return user

    def find_by_email(self, email: str) -> User:
        user_data = self.collection.find_one({"email": email})
        if user_data:
            return User(**user_data) 
        return None
