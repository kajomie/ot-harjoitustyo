from database_connection import get_database_connection
from classes.card import Card

class CardRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_card(self, question, answer, user_id):
        cursor = self._connection.cursor()
        sql = "INSERT INTO cards (question, answer, user_id) VALUES (?, ?, ?)"
        cursor.execute(sql, [question, answer, user_id])

        self._connection.commit()

        card = Card(question, answer)
        return card

    def get_cards(self, user_id):
        cursor = self._connection.cursor()

        sql = "SELECT * FROM cards WHERE cards.user_id = ?"
        cursor.execute(sql, [user_id])
        result = cursor.fetchall()

        return result if result else None
