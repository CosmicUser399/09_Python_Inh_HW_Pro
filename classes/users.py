# 2. Базовый класс User и производные классы для различных типов пользователей

import hashlib
import uuid

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
        return f"Пользователь: {self.username}, Email: {self.email}"




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
                break



class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    def __init__(self):
        pass

    def register(self, user_class, username, email, password, *args):
        """
        Регистрация нового пользователя.
        """
        pass

    def login(self, username, password):
        """
        Аутентификация пользователя.
        """
        pass

    def logout(self):
        """
        Выход пользователя из системы.
        """
        pass

    def get_current_user(self):
        """
        Возвращает текущего вошедшего пользователя.
        """
        pass
