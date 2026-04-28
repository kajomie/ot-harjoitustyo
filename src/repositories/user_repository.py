from classes.user import User

class UserRepository:
    """Käyttäjien datan tallennuksesta huolehtiva luokka.
    """
    def __init__(self, connection):
        """UserRepository-luokan konstruktori.

        Args:
            connection: Tietokantaan luotu yhteys.
        """
        self._connection = connection

    def create_user(self, username, password):
        """Uuden käyttäjän luonti tietokantaan.

        Args:
            username: Käyttäjänimi.
            password: Salasana.

        Returns:
            Palauttaa juuri luodun käyttäjän oliomuodossa.
        """
        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(sql, [username, password])

        self._connection.commit()
        user_id = cursor.lastrowid

        user = User(user_id, username, password)
        return user

    def search_user(self, user):
        """Käyttäjän etsiminen nimen avulla.

        Args:
            user: Etsittävä käyttäjä.

        Returns:
            Palauttaa halutun käyttäjän nimen jos käyttäjä löytyi, ja None jos ei löytynyt.
        """
        cursor = self._connection.cursor()

        sql = "SELECT * FROM users WHERE users.username = ?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()

        return result[0][1] if result else None

    def check_login(self, username, password):
        """Käyttäjänimen ja salasanan olemassaolon tarkistaminen sisäänkirjautumisen yhteydessä.

        Args:
            username: Käyttäjänimi.
            password: Salasana.

        Returns:
            Palauttaa sisäänkirjautuneen käyttäjän jos tiedoille löytyi match tietokannasta.
        """
        cursor = self._connection.cursor()

        sql = "SELECT * FROM users WHERE users.username = ? and users.password = ?"
        cursor.execute(sql, [username, password])
        result = cursor.fetchall()

        return User(result[0][0], result[0][1], result[0][2]) if result else None

    def delete_all_users(self):
        """Jokaisen käyttäjän poisto tietokannasta.
        """
        cursor = self._connection.cursor()
        sql = "DELETE FROM users"
        cursor.execute(sql)

        self._connection.commit()
