from database_connection import get_database_connection
from repositories.user_repository import UserRepository
from repositories.card_repository import CardRepository

class WrongUsernameOrPassword(Exception):
    pass

class UsernameAlreadyInUse(Exception):
    pass

class EmptyNameOrPasswordField(Exception):
    pass

class CardService:
    def __init__(self, user_repository=None):
        self._user = None
        self._user_repository = user_repository if user_repository else UserRepository(get_database_connection())
        self._card_repository = CardRepository(get_database_connection())

    def create_new_user(self, username, password):
        if not username or not password:
            raise EmptyNameOrPasswordField("Käyttäjätunnus tai salasana eivät saa olla tyhjiä!")

        username_available = self._user_repository.search_user(username)
        if username_available:
            raise UsernameAlreadyInUse("Käyttäjänimi on jo varattu!")

        user = self._user_repository.create_user(username, password)
        return user

    def get_user(self):
        return self._user

    def login(self, username, password):
        user = self._user_repository.check_login(username, password)

        if user:
            self._user = user
        else:
            raise WrongUsernameOrPassword("Väärä käyttäjänimi tai salasana!")

        return self._user

    def logout(self):
        self._user = None

    def create_new_card(self, question, answer):
        user_id = self._user.id
        return self._card_repository.create_card(question, answer, user_id)

    def get_cards(self, user):
        user_id = self._user.id
        lista = self._card_repository.get_cards(user_id)
        return lista

card_service = CardService()
