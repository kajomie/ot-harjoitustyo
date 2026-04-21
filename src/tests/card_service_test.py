import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.user_repository import UserRepository
from classes.user import User
from application.card_service import CardService, WrongUsernameOrPassword, UsernameAlreadyInUse, EmptyNameOrPasswordField


class UserRepositoryStub:
    def __init__(self, users=None):
        self.users = users if users else []
        self.id = 1

    def create_user(self, username, password):
        user = User(self.id, username, password)
        self.users.append(user)
        self.id += 1
        return user

    def get_users(self):
        return self.users
    
    def check_login(self, username, password):
        res = [user for user in self.users if user.username == username and user.password == password]

        return res[0] if res else None
    
    def search_user(self, username):
        res = [user for user in self.users if user.username == username]

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

    def test_login_with_wrong_username_raises_error(self):
        self.assertRaises(WrongUsernameOrPassword, lambda: self.card_service.login("jokunimi", "jokusalasana"))

    def test_logout_works(self):
        self.card_service.create_new_user("ihansama", "ihansama")
        self.card_service.login("ihansama", "ihansama")
        self.card_service.logout()
        kayttaja = self.card_service.get_user()
        self.assertEqual(None, kayttaja)

    def test_username_already_used_raises_error(self):
        self.card_service.create_new_user("jokuvaan", "jokuvaan")
        self.assertRaises(UsernameAlreadyInUse, lambda: self.card_service.create_new_user("jokuvaan", "jokusalasana"))

    def test_empty_name_or_password_raises_error(self):
        self.assertRaises(EmptyNameOrPasswordField, lambda: self.card_service.create_new_user("", ""))