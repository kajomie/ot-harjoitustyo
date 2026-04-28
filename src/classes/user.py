class User:
    """Käyttäjää vastaava luokka.
    """
    def __init__(self, id, username, password):
        """User-luokan konstruktori.

        Args:
            id: Käyttäjän id.
            username: Käyttäjänimi.
            password: Salasana.
        """
        self.id = id
        self.username = username
        self.password = password
