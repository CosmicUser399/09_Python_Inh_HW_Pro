from classes.products import Electronics, Clothing
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart

def main():
    
    # Создаем продукты
    laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
    tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")

    # Создаем пользователей
    customer = Customer(username="Mikhail", email="python@derkunov.ru", password="123", address="033 Russ Bur")
    admin = Admin(username="root", email="root@derkunov.ru", password="root", admin_level=5)

    admin.list_users()  # Выводим список всех пользователей
    admin.delete_user("Mikhail")  # Удаляем пользователя Mikhail
    admin.list_users()  # Выводим список всех пользователей после удаления

    # Создаем корзину покупок и добавляем товары
    cart = ShoppingCart()
    cart.add_item(laptop, 1)
    cart.add_item(tshirt, 3)

    # Выводим детали корзины
    print(cart.get_details())

if __name__ == "__main__":
    main()