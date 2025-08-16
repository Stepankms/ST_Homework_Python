from address import Address
from mailing import Mailing

toaddress = Address("681014", "Комсомольск-на-Амуре", "Победы", "22/7", "8")
fromaddress = Address("350024", "Краснодар", "Российская", "267/3, корпус 3", "205")

Mail = Mailing(toaddress, fromaddress, 5600, "QWE123")

print(f"Отправление {Mail.track} из {Mail.from_address.index}, {Mail.from_address.city},"
      f"{Mail.from_address.street}, {Mail.from_address.house} - {Mail.from_address.flat}"
      f"в {Mail.to_address.index}, {Mail.to_address.city}, {Mail.to_address.street},"
      f"{Mail.to_address.house} - {Mail.to_address.flat}. Стоимость {Mail.cost} рублей.")
