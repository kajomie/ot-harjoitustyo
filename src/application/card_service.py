from classes.user import User
from database_connection import get_database_connection
from repositories.user_repository import UserRepository
from repositories.card_repository import CardRepository

class CardService:
    def __init__(self, user_repository=None):
        self._user = None
        self._user_repository = user_repository if user_repository else UserRepository(get_database_connection())
        self._card_repository = CardRepository(get_database_connection())

    def create_new_user(self, username, password):
        user = self._user_repository.create_user(username, password)
        return user

    def get_user(self):
        return self._user

    def login(self, username, password):
        user = self._user_repository.check_login(username, password)

        if user:
            self._user = user

        return self._user

card_service = CardService()
