import getpass
import os
import shutil
import sys

# Эмуляция базы данных пользователей (в реальном проекте используйте хэширование)
USERS_DB = {"admin": "password123", "user": "qwerty"}


def clear_screen():
    """Очистка консоли в зависимости от ОС."""
    os.system("cls" if os.name == "nt" else "clear")


def login():
    """Функция авторизации пользователя."""
    clear_screen()
    print("=== АВТОРИЗАЦИЯ ===")
    username = input("Введите логин: ").strip()
    # getpass скрывает ввод пароля в терминале
    password = getpass.getpass("Введите пароль: ")

    if username in USERS_DB and USERS_DB[username] == password:
        print(f"\n[+] Добро пожаловать, {username}!")
        input("\nНажмите Enter, чтобы продолжить...")
        return True
    else:
        print("\n[-] Неверный логин или пароль!")
        input("\nНажмите Enter, чтобы попробовать снова...")
        return False


def get_disk_info():
    """Получение информации о дисках."""
    clear_screen()
    print("=== ИНФОРМАЦИЯ О ДИСКАХ ===\n")

    # Форматирование вывода (перевод в Гигабайты)
    GB = 1024**3

    if os.name == "nt":
        # Логика для Windows (перебор букв дисков)
        import ctypes

        bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
        for i in range(26):
            if bitmask & (1 << i):
                drive_letter = f"{chr(65 + i)}:\\"
                try:
                    total, used, free = shutil.disk_usage(drive_letter)
                    print(f"Диск: {drive_letter}")
                    print(f"  Всего:   {total / GB:.2f} GB")
                    print(f"  Занято:  {used / GB:.2f} GB")
                    print(f"  Свободно: {free / GB:.2f} GB")
                    print("-" * 30)
                except PermissionError:
                    print(f"Диск: {drive_letter} (Нет доступа)")
                    print("-" * 30)
    else:
        # Логика для Linux / macOS (корневой раздел)
        # В Linux можно также парсить /proc/mounts или использовать psutil
        try:
            total, used, free = shutil.disk_usage("/")
            print("Корневой раздел (/)")
            print(f"  Всего:   {total / GB:.2f} GB")
            print(f"  Занято:  {used / GB:.2f} GB")
            print(f"  Свободно: {free / GB:.2f} GB")
            print("-" * 30)
        except Exception as e:
            print(f"Ошибка получения данных: {e}")

    input("\nНажмите Enter, чтобы вернуться в меню...")


def main_menu():
    """Главное меню после успешного входа."""
    while True:
        clear_screen()
        print("=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Посмотреть информацию о дисках")
        print("2. Выйти из аккаунта")
        print("3. Выйти из программы")

        choice = input("\nВыберите действие (1-3): ").strip()

        if choice == "1":
            get_disk_info()
        elif choice == "2":
            print("\nВыход из аккаунта...")
            break
        elif choice == "3":
            print("\nЗавершение работы. До свидания!")
            sys.exit()
        else:
            print("\n[-] Некорректный ввод!")
            input("Нажмите Enter, чтобы повторить...")


def main():
    """Основной цикл программы."""
    while True:
        clear_screen()
        print("=== КОНСОЛЬНОЕ ПРИЛОЖЕНИЕ ===")
        print("1. Войти в систему")
        print("2. Выйти из программы")

        choice = input("\nВыберите действие (1-2): ").strip()

        if choice == "1":
            if login():
                main_menu()
        elif choice == "2":
            print("\nЗавершение работы. До свидания!")
            break
        else:
            print("\n[-] Некорректный ввод!")
            input("Нажмите Enter, чтобы повторить...")


if __name__ == "__main__":
    main()

