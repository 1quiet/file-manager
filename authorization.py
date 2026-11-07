import hashlib 
import psycopg
import getpass
import subprocess
import sys

DB_CONFIG = {
        "host": "localhost", 
        "dbname": "manager_creds",
        "user": "postgres",
        "password": "postgres",
        "port": "5432"
        }

def hash_pass(password: str, salt: str = None):
    is salt is None:
        salt = os.random(16).hex()
    salted_pass = password + salt
    password_hash = hashlib.sha256(salted_pass.encode()).hexdigest()

    return password_hash, salt

def register_user():
    print("\nRegistry new user!\n")
    username = input("Enter your username: ").strip()
    password = getpass.getpass("Your password: ")
    if not username or not password:
        print("login or password could not be empty!")
        return
    p_hash, salt = hash_pass(password)

    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as curr:
                query = """
                insert into users (username, password_hash, salt)
                values (%s, %s, %s)
                """
                curr.execute(query, (username, p_hash, salt))

                conn.commit()
        print(f"\nUser _{username}_  successfully added!")
        print(f"В бд занесено ({p_hash[:10]}...) и соль {salt[:10]}...")
    except psycopg.errors.UniqueViolation:
        print("Ошибка")
    except Exception as e:
        print("{e}")
    


def verify_login():
    print("Logining page: ")
    input_name = input("Your username: ").strip()
    input_password = getpass.getpass("Your password: ")
    
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as curr:
                query = "SELECT password_hash, salt FROM users WHERE username = %s;"
                curr.execute(query, (input_name,))
                user_data = curr.fetchone()

                if user_data is None:
                    print("Wrong login or password")
                    return False

                stored_hash, stored_salt = user_data

            salted_input = input_password + stored_salt
            calculated_hash = hashlib.sha256(salted_input.encode()).hexdigest()

            if calculated_hash == stored_hash:
                print("Пароли совпадают, вход разрешен!")
                return True
            else:
                print("Неверный логин или пароль")
                return False
    except Exception as e:
        print(f"Ошибка при работе с БД {e}")
        return False

if __name__ == "__main__":
    if verify_login():
        print("Запуск менеджера")
        subprocess.run([sys.executable, "my_try.py"], check=True)

if __name__ == "__main__":
    choice = input("Выберите действие: (1-4)").strip()
    print("\n1. Регистрация (для новых пользователей)")
    print("2. Авторизация")
    print("3. 
    match choice:
        case 1:

