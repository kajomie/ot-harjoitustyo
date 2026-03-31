from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, password):
        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(sql, [username, password])

        self._connection.commit()

    def search_user(self, user):
        cursor = self._connection.cursor()

        sql = "SELECT * FROM users WHERE users.username = ?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()

        return result[0][1] if result else None

    def delete_all_users(self):
        cursor = self._connection.cursor()
        sql = "DELETE FROM users"
        cursor.execute(sql)

        self._connection.commit()