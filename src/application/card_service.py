from database_connection import get_database_connection
from repositories.user_repository import UserRepository
from repositories.card_repository import CardRepository

class WrongUsernameOrPassword(Exception):
    pass

class UsernameAlreadyInUse(Exception):
    pass

class EmptyField(Exception):
    pass

class CardService:
    """Sovelluslogiikkaa hoitava luokka.
    """
    def __init__(self, user_repository=None, card_repository=None):
        """CardService-luokan konstruktori.

        Args:
            user_repository: Käyttäjärepositorio. Jos olio ei ole jo olemassa niin se luodaan.
        """
        self._user = None
        self._user_repository = user_repository if user_repository \
            else UserRepository(get_database_connection())
        self._card_repository = card_repository if card_repository \
            else CardRepository(get_database_connection())

    def create_new_user(self, username, password):
        """Uuden käyttäjän luonti.

        Args:
            username: Käyttäjänimi.
            password: Salasana.

        Raises:
            EmptyField: Virhe, joka tulee jos käyttäjänimi tai salasana ovat tyhjiä.
            UsernameAlreadyInUse: Virhe, joka tulee jos käyttäjänimi on jo käytössä.

        Returns:
            Palauttaa juuri luodun käyttäjän oliona.
        """
        if not username or not password:
            raise EmptyField("Käyttäjätunnus tai salasana eivät saa olla tyhjiä!")

        username_available = self._user_repository.search_user(username)
        if username_available:
            raise UsernameAlreadyInUse("Käyttäjänimi on jo varattu!")

        user = self._user_repository.create_user(username, password)
        return user

    def get_user(self):
        """Palauttaa nykyisen sisäänkirjautuneen käyttäjän.

        Returns:
            Palauttaa nykyisen käyttäjän oliona.
        """
        return self._user

    def login(self, username, password):
        """Sisäänkirjautuminen.

        Args:
            username: Käyttäjänimi.
            password: Salasana.

        Raises:
            WrongUsernameOrPassword: Virhe, joka tulee jos käyttäjänimi tai salasana on väärin.

        Returns:
            Palauttaa käyttäjän oliona, jos kirjautuminen onnistuu.
        """
        user = self._user_repository.check_login(username, password)

        if user:
            self._user = user
        else:
            raise WrongUsernameOrPassword("Väärä käyttäjänimi tai salasana!")

        return self._user

    def logout(self):
        """Uloskirjautuminen.
        """
        self._user = None

    def create_new_card(self, question, answer, deck_id):
        """Uuden muistikortin luonti.

        Args:
            question; Kysymys.
            answer: Vastaus.
            deck_id: Pakan id.

        Returns:
            Palauttaa juuri luodun kortin oliona.
        """
        if not question or not answer or not deck_id:
            raise EmptyField("Kortin kysymys, vastaus tai pakka eivät saa olla tyhjiä!")

        user_id = self._user.id
        return self._card_repository.create_card(question, answer, user_id, deck_id)

    def get_cards(self, user):
        """Käyttäjän korttien palautus.

        Args:
            user: Käyttäjä, joka on luonut kortit.

        Returns:
            Palauttaa listan käyttäjän korteista.
        """
        user_id = self._user.id
        cardlist = self._card_repository.get_cards(user_id)
        return cardlist

    def create_new_deck(self, name):
        """Uuden pakan luonti.

        Args:
            name: Pakan nimi.

        Returns:
            Palauttaa juuri luodun pakan oliona.
        """
        if not name:
            raise EmptyField("Pakan nimi ei saa olla tyhjä!")

        user_id = self._user.id
        deck = self._card_repository.create_deck(name, user_id)
        return deck

    def delete_card(self, card_id):
        """Yksittäisen kortin poisto.

        Args:
            card_id: Poistettavan kortin id.
        """
        self._card_repository.delete_card(card_id)

    def get_decks(self, user):
        """Käyttäjän pakkojen palautus.

        Args:
            user: Käyttäjä, joka on luonut pakat..

        Returns:
            Palauttaa listan käyttäjän pakoista.
        """
        user_id = self._user.id
        decklist = self._card_repository.get_decks(user_id)
        return decklist

    def get_deck_cards(self, deck_id):
        """Palauttaa tietyn pakan kortit.

        Args:
            deck_id: Pakan id.

        Returns:
            Palauttaa pakan kortit listana.
        """
        decklist = self._card_repository.get_deck_cards(deck_id)
        return decklist

    def edit_card(self, card_id, question, answer, user_id, deck_id):
        """Kortin muokkaus.

        Args:
            card_id: Muokattavan kortin id.
            question: Kortin kysymys.
            answer: Kortin vastaus.
            user_id: Kortin luoneen käyttäjän id.
            deck_id: Kortin pakan id.

        Raises:
            EmptyField: Virhe, joka nostetaan jos kysymys tai vastaus ovat tyhjiä.

        Returns:
            Palauttaa muokatun kortin oliona.
        """
        if not question or not answer or not deck_id:
            raise EmptyField("Kortin kysymys, vastaus tai pakka eivät saa olla tyhjiä!")

        edited_card = self._card_repository.edit_card(card_id, question, answer, user_id, deck_id)
        return edited_card

card_service = CardService()
