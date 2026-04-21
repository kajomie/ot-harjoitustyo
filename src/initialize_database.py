from database_connection import get_database_connection

def delete_tables(connection):
    cursor = connection.cursor()

    sql = "DROP TABLE IF EXISTS users;"
    cursor.execute(sql)

    sql2 = "DROP TABLE IF EXISTS cards;"
    cursor.execute(sql2)

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    sql = "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);"
    cursor.execute(sql)

    sql2 = "CREATE TABLE cards (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, user_id INTEGER REFERENCES users);"
    cursor.execute(sql2)

    connection.commit()

def initialize_database():
    connection = get_database_connection()
    delete_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
