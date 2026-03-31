import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(get_database_connection())
        self.user_repository.delete_all_users()

    def test_creating_user_works(self):
        testikayttaja = self.user_repository.create_user("kissa", "salasana")
        haku = self.user_repository.search_user("kissa")

        self.assertEqual(haku, "kissa")