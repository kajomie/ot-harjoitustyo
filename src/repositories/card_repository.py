from classes.card import Card
from classes.deck import Deck

class CardRepository:
    """Kortteihin ja pakkoihin liittyvän datan tallennuksen hoitava luokka.
    """
    def __init__(self, connection):
        """CardRepository-luokan konstruktori.

        Args:
            connection: Tietokantayhteys.
        """
        self._connection = connection

    def create_card(self, question, answer, user_id, deck_id):
        """Uuden kortin luonti.

        Args:
            question: Kysymys.
            answer: Vastaus.
            user_id: Kortin luoneen käyttäjän id.
            deck_id: Kortin pakan id.

        Returns:
            Palauttaa juuri luodun kortin oliomuodossa.
        """
        cursor = self._connection.cursor()
        sql = "INSERT INTO cards (question, answer, user_id, deck_id) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, [question, answer, user_id, deck_id])

        self._connection.commit()
        card_id = cursor.lastrowid

        card = Card(card_id, question, answer, user_id, deck_id)
        return card

    def get_cards(self, user_id):
        """Käyttäjän korttien palautus.

        Args:
            user_id: Käyttäjän id.

        Returns:
            Palauttaa listan käyttäjän luomista korteista jos niitä on, muuten tyhjän listan.
        """
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
        """Uuden pakan luonti.

        Args:
            name: Pakan nimi.
            user_id: Pakan luoneen käyttäjän id.

        Returns:
            Palauttaa luodun pakan oliona.
        """
        cursor = self._connection.cursor()
        sql = "INSERT INTO decks (name, user_id) VALUES (?, ?)"
        cursor.execute(sql, [name, user_id])

        self._connection.commit()
        deck_id = cursor.lastrowid

        deck = Deck(deck_id, name, user_id)
        return deck

    def get_decks(self, user_id):
        """Käyttäjän pakkojen palautus.

        Args:
            user_id: Käyttäjä-id.

        Returns:
            Palauttaa listan käyttäjän pakoista jos niitä on, muuten palauttaa tyhjän listan.
        """
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
        """Kortin pakan palautus.

        Args:
            card_id: Kortin id.

        Returns:
            Palauttaa pakan jos kortin pakka on olemassa, muuten None.
        """
        cursor = self._connection.cursor()

        sql = """SELECT decks.id, decks.name, decks.user_id FROM decks, cards
        WHERE decks.id = cards.deck_id
        AND cards.id = ?"""
        cursor.execute(sql, [card_id])
        result = cursor.fetchall()

        return Deck(result[0][0], result[0][1], result[0][2]) if result else None

    def get_deck_cards(self, deck_id):
        """Pakan kaikkien korttien palautus.

        Args:
            deck_id: Pakan id.

        Returns:
            Palauttaa listan pakan korteista jos niitä on, muuten palauttaa tyhjän listan.
        """
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

    def delete_card(self, card_id):
        """Yksittäisen kortin poisto.
        """
        cursor = self._connection.cursor()
        sql = "DELETE FROM cards WHERE cards.id = ?"
        cursor.execute(sql, [card_id])

        self._connection.commit()

    def delete_all_cards(self):
        """Kaikkien korttien poisto tietokannasta.
        """
        cursor = self._connection.cursor()
        sql = "DELETE FROM cards"
        cursor.execute(sql)

        self._connection.commit()

    def delete_all_decks(self):
        """Kaikkien pakkojen poisto tietokannasta.
        """
        cursor = self._connection.cursor()
        sql = "DELETE FROM decks"
        cursor.execute(sql)

        self._connection.commit()

    def edit_card(self, card_id, question, answer, user_id, deck_id):
        """Kortin muokkaaminen.

        Args:
            card_id: Kortin id.
            question: Kortin kysymys.
            answer: Kortin vastaus.
            user_id: Kortin luoneen käyttäjän id.
            deck_id: Kortin pakan id.

        Returns:
            Palauttaa muokatun kortin oliona.
        """
        cursor = self._connection.cursor()
        sql = """UPDATE cards SET question = ?, answer = ?, deck_id = ?
        WHERE cards.id = ?
        AND cards.user_id = ?"""
        cursor.execute(sql, [question, answer, deck_id, card_id, user_id])

        self._connection.commit()

        card = Card(card_id, question, answer, user_id, deck_id)
        return card
