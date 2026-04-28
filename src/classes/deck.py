class Deck:
    """Pakkaa vastaava luokka.
    """
    def __init__(self, id, name, user_id):
        """Deck-luokan konstruktori.

        Args:
            id: Pakan id.
            name: Pakan nimi.
            user_id: Pakan luoneen käyttäjän id.
        """
        self.id = id
        self.name = name
        self.user_id = user_id
