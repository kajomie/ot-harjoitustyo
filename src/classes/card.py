class Card:
    """Korttia vastaava luokka.
    """
    def __init__(self, id, question, answer, user_id, deck_id):
        """Card-luokan konstruktori.

        Args:
            id: Kortin id.
            question: Kysymys.
            answer: Vastaus.
            user_id: Kortin luoneen käyttäjän id.
            deck_id: Kortin pakan id.
        """
        self.id = id
        self.question = question
        self.answer = answer
        self.user_id = user_id
        self.deck_id = deck_id
