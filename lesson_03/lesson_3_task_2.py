from smartphone import Smartphone

# Создаем список самртфонов
library = [
    Smartphone("Nokia", "2110", "+79951691288"),
    Smartphone("Iphone", "16", "+79964117538"),
    Smartphone("Xiaomi", "Redmi 12", "+79811234578"),
    Smartphone("OnePlus", "22", "+79811234579"),
    Smartphone("Samsung", "S22", "+79811235579")
]

# Печатаем список
for smartphone in library:
    print(f"{smartphone.title} - {smartphone.model} - {smartphone.number}")
