import sqlite3
from random import randint



database_1 = sqlite3.connect('server.sqlite3')
sql = database_1.cursor()

sql.execute(
    """CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash INT 
    )
    """

)
database_1.commit()


def register_user():
    global user_login, user_password, balance
    user_login = input('login: ')
    user_password = input('password: ')

    sql.execute(f' S'
                f'')
    sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
    database_1.commit()
    print('User registered')
    for value in sql.execute("SELECT login FROM users"):
        print(value)

if __name__ == "__main__":
    register_user()

