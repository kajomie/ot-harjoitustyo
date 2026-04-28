import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.user_repository import UserRepository
from repositories.card_repository import CardRepository
from classes.card import Card
from classes.deck import Deck

class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(get_database_connection())
        self.user_repository.delete_all_users()
        self.card_repository = CardRepository(get_database_connection())
        self.card_repository.delete_all_decks()
        self.card_repository.delete_all_cards()

    def test_creating_card_works(self):
        testikortti = self.card_repository.create_card("moi", "jotain", 1, 1)
        toinen_kortti = self.card_repository.get_cards(1)

        self.assertEqual(testikortti.question, toinen_kortti[0].question)

    def test_creating_deck_works(self):
        testipakka = self.card_repository.create_deck("testipakka", 1)
        toinen_pakka = self.card_repository.get_decks(1)

        self.assertEqual(testipakka.name, toinen_pakka[0].name)