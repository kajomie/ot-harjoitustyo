import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.user_repository import UserRepository
from classes.user import User
from application.card_service import CardService


class UserRepositoryStub:
    def __init__(self, users=None):
        self.users = users if users else []

    def create_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        return user

    def get_users(self):
        return self.users
    
    def check_login(self, username, password):
        res = [user for user in self.users if user.username == username and user.password == password]

        return res[0] if res else None


class TestCardService(unittest.TestCase):
    def setUp(self):
        self.card_service = CardService(UserRepositoryStub())

    def test_create_user_works(self):
        kayttaja = self.card_service.create_new_user("testikayttaja", "salasana123")
        self.assertEqual("testikayttaja", kayttaja.username)

    def test_login_works(self):
        self.card_service.create_new_user("jokukayttaja", "testisalasana")
        testikayttaja = self.card_service.login("jokukayttaja", "testisalasana")
        self.assertEqual("jokukayttaja", testikayttaja.username)
        self.assertEqual("testisalasana", testikayttaja.password)

    def test_get_user_works(self):
        self.card_service.create_new_user("joku", "jotain")
        self.card_service.login("joku", "jotain")
        kayttaja = self.card_service.get_user()
        self.assertEqual("joku", kayttaja.username)