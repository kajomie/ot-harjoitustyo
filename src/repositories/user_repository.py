from database_connection import get_database_connection
from classes.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, password):
        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(sql, [username, password])

        self._connection.commit()

        user = User(username, password)
        return user

    def search_user(self, user):
        cursor = self._connection.cursor()

        sql = "SELECT * FROM users WHERE users.username = ?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()

        return result[0][1] if result else None

    def check_login(self, username, password):
        cursor = self._connection.cursor()

        sql = "SELECT * FROM users WHERE users.username = ? and users.password = ?"
        cursor.execute(sql, [username, password])
        result = cursor.fetchall()

        return User(result[0][1], result[0][2]) if result else None

    def delete_all_users(self):
        cursor = self._connection.cursor()
        sql = "DELETE FROM users"
        cursor.execute(sql)

        self._connection.commit()
