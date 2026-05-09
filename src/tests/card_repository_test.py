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

    def test_get_deck_works(self):
        testipakka = self.card_repository.create_deck("testipakka", 1)
        testikortti = self.card_repository.create_card("moi", "jotain", 1, testipakka.id)
        haettupakka = self.card_repository.get_deck(testikortti.id)

        self.assertEqual(testipakka.id, haettupakka.id)

    def test_get_decks_work(self):
        self.card_repository.create_deck("ekapakka", 1)
        self.card_repository.create_deck("tokapakka", 1)

        haetutpakat = len(self.card_repository.get_decks(1))

        self.assertEqual(haetutpakat, 2)

    def test_get_deck_cards_works(self):
        self.card_repository.create_card("ekakysymys", "ekavastaus", 1, 1)
        self.card_repository.create_card("tokakysymys", "tokavastaus", 1, 1)
        self.card_repository.create_card("kolmaskysymys", "kolmasvastaus", 1, 1)

        haetutkortit = len(self.card_repository.get_deck_cards(1))

        self.assertEqual(haetutkortit, 3)

    def test_deleting_card_works(self):
        testikortti = self.card_repository.create_card("moro", "jokuvastaus", 1, 1)
        self.card_repository.delete_card(testikortti.id)
        kaikkikortit = len(self.card_repository.get_cards(1))

        self.assertEqual(kaikkikortit, 0)

    def test_editing_card_works(self):
        testikortti = self.card_repository.create_card("kysymys", "vastaus", 1, 1)
        editoitu = self.card_repository.edit_card(testikortti.id, "muokattukysymys", "muokattuvastaus", 1, 1)

        self.assertEqual(editoitu.question, "muokattukysymys")
        self.assertEqual(editoitu.answer, "muokattuvastaus")