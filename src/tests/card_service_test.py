import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.user_repository import UserRepository
from classes.user import User
from classes.card import Card
from classes.deck import Deck
from application.card_service import CardService, WrongUsernameOrPassword, UsernameAlreadyInUse, EmptyField


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

class CardRepositoryStub:
    def __init__(self, cards=None, decks=None):
        self.cards = cards if cards else []
        self.decks = decks if decks else []
        self.card_id = 1
        self.deck_id = 1

    def create_card(self, question, answer, user_id, deck_id):
        card = Card(self.card_id, question, answer, user_id, deck_id)
        self.card_id += 1
        self.cards.append(card)
        return card

    def get_cards(self, user_id):
        res = [card for card in self.cards if card.user_id == user_id]

        return res if res else []

    def create_deck(self, name, user_id):
        deck = Deck(self.deck_id, name, user_id)
        self.deck_id += 1
        self.decks.append(deck)
        return deck

    def get_decks(self, user_id):
        res = [deck for deck in self.decks if deck.user_id == user_id]

        return res if res else []

    def get_deck(self, card_id):
        card = [card for card in self.cards if card.id == card_id]
        card_deck = card[4]
        res = [deck for deck in self.decks if deck.id == card_deck]

        return res[0] if res else None

    def get_deck_cards(self, deck_id):
        res = [card for card in self.cards if card.deck_id == deck_id]

        return res if res else []

    def delete_card(self, card_id):
        self.cards = [card for card in self.cards if card.id != card_id]

    def delete_all_cards(self):
        self.cards = []

    def delete_all_decks(self):
        self.decks = []

    def edit_card(self, card_id, question, answer, user_id, deck_id):
        edited_card = None

        for card in self.cards:
            if card.id == card_id:
                card.question = question
                card.answer = answer
                edited_card = card

        return edited_card


class TestCardService(unittest.TestCase):
    def setUp(self):
        self.card_service = CardService(UserRepositoryStub(), CardRepositoryStub())

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
        self.assertRaises(EmptyField, lambda: self.card_service.create_new_user("", ""))

    def test_empty_fields_when_creating_card_raises_error(self):
        self.assertRaises(EmptyField, lambda: self.card_service.create_new_card("", "", ""))

    def test_empty_name_when_creating_deck_raises_error(self):
        self.assertRaises(EmptyField, lambda: self.card_service.create_new_deck(""))

    def test_create_new_card_works(self):
        self.card_service.create_new_user("testikayttaja456", "jokusalasana")
        self.card_service.login("testikayttaja456", "jokusalasana")
        user = self.card_service.get_user()

        deck = self.card_service.create_new_deck("testipakka")
        self.card_service.create_new_card("jokukysymys", "jokuvastaus", deck.id)
        searched_cards = len(self.card_service.get_cards(user.id))
        self.assertEqual(searched_cards, 1)

    def test_create_new_deck_works(self):
        self.card_service.create_new_user("testikayttaja123", "jotainvaan")
        self.card_service.login("testikayttaja123", "jotainvaan")
        user = self.card_service.get_user()

        self.card_service.create_new_deck("jokupakka")
        searched_decks = len(self.card_service.get_decks(user.id))
        self.assertEqual(searched_decks, 1)
    
    def test_get_deck_cards_works(self):
        self.card_service.create_new_user("testikayttaja123", "jotainvaan")
        self.card_service.login("testikayttaja123", "jotainvaan")

        deck = self.card_service.create_new_deck("jokupakka")
        self.card_service.create_new_card("jokukysymys", "jokuvastaus", deck.id)
        self.card_service.create_new_card("testikysymys", "testivastaus", deck.id)
        deck_cards = len(self.card_service.get_deck_cards(deck.id))
        self.assertEqual(deck_cards, 2)

    def test_delete_card_works(self):
        self.card_service.create_new_user("testikayttaja456", "jokusalasana")
        self.card_service.login("testikayttaja456", "jokusalasana")
        user = self.card_service.get_user()

        deck = self.card_service.create_new_deck("testipakka")
        new_card = self.card_service.create_new_card("jokukysymys", "jokuvastaus", deck.id)
        searched_cards = len(self.card_service.get_cards(user.id))
        self.assertEqual(searched_cards, 1)

        self.card_service.delete_card(new_card.id)
        cards_after_delete = len(self.card_service.get_cards(user.id))
        self.assertEqual(cards_after_delete, 0)

    def test_edit_card_works(self):
        self.card_service.create_new_user("testikayttaja456", "jokusalasana")
        self.card_service.login("testikayttaja456", "jokusalasana")
        user = self.card_service.get_user()

        deck = self.card_service.create_new_deck("testipakka")
        new_card = self.card_service.create_new_card("jokukysymys", "jokuvastaus", deck.id)

        edited_card = self.card_service.edit_card(new_card.id, "muokattu kysymys", "muokattu vastaus", user.id, deck.id)
        self.assertEqual(edited_card.question, "muokattu kysymys")
        self.assertEqual(edited_card.answer, "muokattu vastaus")

    def test_editing_cards_with_empty_fields_raises_error(self):
        self.card_service.create_new_user("testikayttaja456", "jokusalasana")
        self.card_service.login("testikayttaja456", "jokusalasana")
        user = self.card_service.get_user()

        deck = self.card_service.create_new_deck("testipakka")
        new_card = self.card_service.create_new_card("jokukysymys", "jokuvastaus", deck.id)

        self.assertRaises(EmptyField, lambda: self.card_service.edit_card(new_card.id, "", "", "", user.id))