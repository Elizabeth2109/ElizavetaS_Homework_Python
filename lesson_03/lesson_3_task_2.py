from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 16 Pro", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S21 Ultra", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 6", "+79456789012"))
catalog.append(Smartphone("Poco", "M 6", "+79567890123"))

for phone in catalog:
    print(phone)
