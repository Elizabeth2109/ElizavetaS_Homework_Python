from user import User
from card import Card

richard = User("Richard")

richard.sayName()
richard.setAge(23)
richard.sayAge()

card = Card("1234 5678 8765 4321", "03/28", "Richard S")
richard.addCard(card)
richard.getCard().pay(2352)
