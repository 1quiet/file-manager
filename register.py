import hashlib
import os
import psycopg

DB_CONFIG = {
        "host": "localhost",
        "dbname": "manager_creds",
        "user": "postgres",
        "password": "postgres",
        "port": "5432"
        }

def hash_pass (password: str, salt: str = None):
    if salt is None:
        salt = os.urandom(16).hex()

    salted_pass = password + salt
    password_hash = hashlib.sha256(salted_pass.encode()).hexdigest()

    return password_hash, salt

def register_user():
    print("Регистрация нового пользователя")
    username = input("введите желаемый логин: ").strip()
    password = input("enter your password: ").strip()

    if not username or not password:
        print("login or password could not be empty")
        return
    p_hash, salt = hash_pass(password)
    

    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                query = """
                    insert into users (username, password_hash, salt)
                    values (%s, %s, %s);
                    """
                cur.execute(query, (username, p_hash, salt))

                conn.commit()
        print(f"\nПользователь '{username}' успешно зарегистрирован")
        print(f"В БД занесено: ({p_hash[10:]}...) \nи соль ({salt[10:]}...)")
    except psycopg.errors.UniqueViolation:
              print(f"Ошибка такой логин уже зареган")
    except Exception as e:
              print(f"не удалось подключиться к БД или ошибка {e}")

if __name__ == "__main__":
    register_user()
                
