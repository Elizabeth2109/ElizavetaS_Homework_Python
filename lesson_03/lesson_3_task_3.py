from address import Address
from mailing import Mailing

from_addr = Address(123456, "Москва", "Тверская ул.", "9", "15")
to_addr = Address(789012, "Санкт-Петербург", "Невский пр.", "27", "7")

mailing_instance = Mailing(to_addr, from_addr, 1540.70, "RU123456789")

print(
    f"Отправление {mailing_instance.track} из {mailing_instance.from_address}"
    f" в {mailing_instance.to_address}. Стоимость {mailing_instance.cost} руб."
)
