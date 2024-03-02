from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def find_by_email(self, email: str):
        pass
