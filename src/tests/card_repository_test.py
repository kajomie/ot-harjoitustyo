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
        newcard = self.card_repository.create_card("moi", "jotain", 1, 1)
        othercard = self.card_repository.get_cards(1)

        self.assertEqual(newcard.question, othercard[0].question)

    def test_creating_deck_works(self):
        newdeck = self.card_repository.create_deck("uusipakka", 1)
        otherdeck = self.card_repository.get_decks(1)

        self.assertEqual(newdeck.name, otherdeck[0].name)

    def test_get_deck_works(self):
        newdeck = self.card_repository.create_deck("uusipakka", 1)
        newcard = self.card_repository.create_card("moi", "jotain", 1, newdeck.id)
        searched_deck = self.card_repository.get_deck(newcard.id)

        self.assertEqual(newdeck.id, searched_deck.id)

    def test_get_decks_works(self):
        self.card_repository.create_deck("ekapakka", 1)
        self.card_repository.create_deck("tokapakka", 1)

        searched_decks = len(self.card_repository.get_decks(1))

        self.assertEqual(searched_decks, 2)

    def test_get_decks_works_with_when_not_found(self):
        self.card_repository.create_deck("ekapakka", 1)

        searched_decks = len(self.card_repository.get_decks(2))

        self.assertEqual(searched_decks, 0)

    def test_get_deck_cards_works(self):
        self.card_repository.create_card("ekakysymys", "ekavastaus", 1, 1)
        self.card_repository.create_card("tokakysymys", "tokavastaus", 1, 1)
        self.card_repository.create_card("kolmaskysymys", "kolmasvastaus", 1, 1)

        searched_cards = len(self.card_repository.get_deck_cards(1))

        self.assertEqual(searched_cards, 3)

    def test_get_deck_cards_works_when_not_found(self):
        self.card_repository.create_card("ekakysymys", "ekavastaus", 1, 1)

        searched_cards = len(self.card_repository.get_deck_cards(2))

        self.assertEqual(searched_cards, 0)

    def test_deleting_card_works(self):
        newcard = self.card_repository.create_card("moro", "jokuvastaus", 1, 1)
        self.card_repository.delete_card(newcard.id)
        allcards = len(self.card_repository.get_cards(1))

        self.assertEqual(allcards, 0)

    def test_editing_card_works(self):
        newcard = self.card_repository.create_card("kysymys", "vastaus", 1, 1)
        editedcard = self.card_repository.edit_card(newcard.id, "muokattukysymys", "muokattuvastaus", 1, 1)

        self.assertEqual(editedcard.question, "muokattukysymys")
        self.assertEqual(editedcard.answer, "muokattuvastaus")