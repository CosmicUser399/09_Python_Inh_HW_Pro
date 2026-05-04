# 2. Базовый класс User и производные классы для различных типов пользователей

import hashlib
#import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    
    users = []  # Список для хранения всех пользователей
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        User.users.append(self)  # Добавляем пользователя в список при создании
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """
        return stored_password == User.hash_password(provided_password)

    def get_details(self):
        return f"\nПользователь: {self.username}, Email: {self.email}"


class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"


class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}"
    
    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        print(f"\nВсего пользователей: {len(User.users)}")  # Добавим отладочную информацию
        for user in User.users:
            print(user.get_details())

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """
        for user in User.users:
            if user.username == username:
                User.users.remove(user)
                print(f"\nПользователь {username} удален.")
                break


class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    def __init__(self):
        self.current_user = None  # Текущий авторизованный пользователь
        self.is_authenticated = False  # Флаг авторизации

    def register(self, user_class, username, email, password, *args):
        """
        Регистрация нового пользователя.
        """
        # Проверяем, не занято ли имя пользователя
        for user in User.users:
            if user.username == username:
                return f"Ошибка: пользователь с именем '{username}' уже существует"
        
        # Хешируем пароль перед сохранением
        hashed_password = User.hash_password(password)
        
        # Создаем пользователя соответствующего класса
        if user_class == "customer" or user_class == Customer:
            address = args[0] if args else ""
            new_user = Customer(username, email, hashed_password, address)
        elif user_class == "admin" or user_class == Admin:
            admin_level = args[0] if args else 1
            new_user = Admin(username, email, hashed_password, admin_level)
        else:
            return f"\nОшибка: неизвестный тип пользователя '{user_class}'"
        
        return f"\nПользователь '{username}' успешно зарегистрирован"

    def login(self, username, password):
        """
        Аутентификация пользователя.
        """
        # Ищем пользователя по имени
        for user in User.users:
            if user.username == username:
                # Проверяем пароль
                if User.check_password(user.password, password):
                    self.current_user = user
                    self.is_authenticated = True
                    return f"\nВход выполнен успешно. Добро пожаловать, {username}!"
                else:
                    return "\nОшибка: неверный пароль"
        
        return f"\nОшибка: пользователь '{username}' не найден"

    def logout(self):
        """
        Выход пользователя из системы.
        """
        if self.is_authenticated:
            username = self.current_user.username
            self.current_user = None
            self.is_authenticated = False
            return f"\nПользователь '{username}' вышел из системы"
        else:
            return "Ошибка: нет активной сессии"

    def get_current_user(self):
        """
        Возвращает текущего вошедшего пользователя.
        """
        if self.is_authenticated:
            return self.current_user
        else:
            return None