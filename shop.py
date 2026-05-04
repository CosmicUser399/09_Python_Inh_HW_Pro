from classes.products import Electronics, Clothing
from classes.users import Customer, Admin, AuthenticationService
from classes.shoping_carts import ShoppingCart

def main():
    
    print("1. Проверка функционала классов User, Customer, Admin")
    
    # Создаем продукты
    laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
    tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")

    # Создаем пользователей
    customer = Customer(username="Robert", email="python@robert.ru", password="123", address="033 Russ Bur")
    admin = Admin(username="root", email="root@test.ru", password="root", admin_level=5)

    # Создаем корзину покупок и добавляем товары
    cart = ShoppingCart()
    cart.add_item(laptop, 1)
    cart.add_item(tshirt, 3)

    # Выводим детали корзины
    print(cart.get_details())



    admin.list_users()  # Выводим список всех пользователей
    admin.delete_user("Robert")  # Удаляем пользователя Robert
    admin.list_users()  # Выводим список всех пользователей после удаления

   
    print("\n2. Проверка функционала класса AuthenticationService")
    
    # Создаем сервис авторизации
    auth_service = AuthenticationService()
    
    # Регистрируем нового клиента
    print(auth_service.register(Customer, "Ivan", "ivan@example.com", "password123", "ул. Пушкина, д. 10"))
    
    # Регистрируем администратора
    print(auth_service.register(Admin, "admin", "admin@shop.com", "admin123", 5))
    
    # Пытаемся войти
    print(auth_service.login("Ivan", "wrong_password"))
    print(auth_service.login("unknown_user", "password123"))
    print(auth_service.login("Ivan", "password123"))
    
    # Получаем текущего пользователя
    current_user = auth_service.get_current_user()
    if current_user:
        print(f"\nТекущий пользователь: {current_user.get_details()}")
    
    # Выходим из системы
    print(auth_service.logout())
    
    # Просматриваем всех пользователей
    Admin.list_users()    
    

if __name__ == "__main__":
    main()