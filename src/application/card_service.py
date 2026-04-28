from database_connection import get_database_connection
from repositories.user_repository import UserRepository
from repositories.card_repository import CardRepository

class WrongUsernameOrPassword(Exception):
    pass

class UsernameAlreadyInUse(Exception):
    pass

class EmptyNameOrPasswordField(Exception):
    pass

class CardService:
    """Sovelluslogiikkaa hoitava luokka.
    """
    def __init__(self, user_repository=None):
        """CardService-luokan konstruktori.

        Args:
            user_repository: Käyttäjärepositorio. Jos olio ei ole jo olemassa niin se luodaan.
        """
        self._user = None
        self._user_repository = user_repository if user_repository else UserRepository(get_database_connection())
        self._card_repository = CardRepository(get_database_connection())

    def create_new_user(self, username, password):
        """Uuden käyttäjän luonti.

        Args:
            username: Käyttäjänimi.
            password: Salasana.

        Raises:
            EmptyNameOrPasswordField: Virhe, joka tulee jos käyttäjänimi tai salasana ovat tyhjiä.
            UsernameAlreadyInUse: Virhe, joka tulee jos käyttäjänimi on jo käytössä.

        Returns:
            Palauttaa juuri luodun käyttäjän oliona.
        """
        if not username or not password:
            raise EmptyNameOrPasswordField("Käyttäjätunnus tai salasana eivät saa olla tyhjiä!")

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
        lista = self._card_repository.get_cards(user_id)
        return lista

    def create_new_deck(self, name):
        """Uuden pakan luonti.

        Args:
            name: Pakan nimi.

        Returns:
            Palauttaa juuri luodun pakan oliona.
        """
        user_id = self._user.id
        pakka = self._card_repository.create_deck(name, user_id)
        return pakka

    def get_decks(self, user):
        """Käyttäjän pakkojen palautus.

        Args:
            user: Käyttäjä, joka on luonut pakat..

        Returns:
            Palauttaa listan käyttäjän pakoista.
        """
        user_id = self._user.id
        lista = self._card_repository.get_decks(user_id)
        return lista

card_service = CardService()
