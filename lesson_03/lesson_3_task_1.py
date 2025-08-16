from user import User

# Создаем экземпляр класса User
my_user = User("Ivan", "Ivanov")

# Вызываем методы и выводим результаты
print(my_user.get_first_name())  # Ожидаемый результат: "Ivan"
print(my_user.get_last_name())  # Ожидаемый результат: "Ivanov"
print(my_user.get_user_info())  # Ожидаемый результат: "Ivan Ivanov"
