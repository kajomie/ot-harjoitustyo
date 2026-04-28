from classes.card import Card
from classes.deck import Deck

class CardRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_card(self, question, answer, user_id, deck_id):
        cursor = self._connection.cursor()
        sql = "INSERT INTO cards (question, answer, user_id, deck_id) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, [question, answer, user_id, deck_id])

        self._connection.commit()
        card_id = cursor.lastrowid

        card = Card(card_id, question, answer, user_id, deck_id)
        return card

    def get_cards(self, user_id):
        cursor = self._connection.cursor()

        sql = "SELECT * FROM cards WHERE cards.user_id = ?"
        cursor.execute(sql, [user_id])
        result = cursor.fetchall()
        lista = []

        if result:
            for c in result:
                card = Card(c[0], c[1], c[2], c[3], c[4])
                lista.append(card)

        return lista

    def create_deck(self, name, user_id):
        cursor = self._connection.cursor()
        sql = "INSERT INTO decks (name, user_id) VALUES (?, ?)"
        cursor.execute(sql, [name, user_id])

        self._connection.commit()
        deck_id = cursor.lastrowid

        deck = Deck(deck_id, name, user_id)
        return deck

    def get_decks(self, user_id):
        cursor = self._connection.cursor()

        sql = "SELECT * FROM decks WHERE decks.user_id = ?"
        cursor.execute(sql, [user_id])
        result = cursor.fetchall()
        lista = []

        if result:
            for c in result:
                deck = Deck(c[0], c[1], c[2])
                lista.append(deck)

        return lista

    def get_deck(self, card_id):
        cursor = self._connection.cursor()

        sql = """SELECT decks.id, decks.name, decks.user_id FROM decks, cards
        WHERE decks.id = cards.deck_id
        AND cards.id = ?"""
        cursor.execute(sql, [card_id])
        result = cursor.fetchall()

        return Deck(result[0][0], result[0][1], result[0][2]) if result else None

    def get_deck_cards(self, deck_id):
        cursor = self._connection.cursor()

        sql = "SELECT * FROM cards WHERE cards.deck_id = ?"
        cursor.execute(sql, [deck_id])
        result = cursor.fetchall()
        lista = []

        if result:
            for c in result:
                card = Card(c[0], c[1], c[2], c[3], c[4])
                lista.append(card)

        return lista

    def delete_all_cards(self):
        cursor = self._connection.cursor()
        sql = "DELETE FROM cards"
        cursor.execute(sql)

        self._connection.commit()

    def delete_all_decks(self):
        cursor = self._connection.cursor()
        sql = "DELETE FROM decks"
        cursor.execute(sql)

        self._connection.commit()
