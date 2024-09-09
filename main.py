#!/usr/bin/python3

import models
from models.user import User
from models.product import Product
from models.category import Category
from models.order import Order
from models.order_item import Order_item
from models.cart import Cart
from models.cart_item import Cart_item
from models.favorite import Favorite
from models import storage


amine = User(email="amine@test.com", password="test", username="amine")
amine.save()

ayoub = User(email="ayoub@test.com", password="test", username="ayoub")
ayoub.save()

mohamed = User(email="mohamed@test.com", password="test", username="moahmed")
mohamed.save()

yahya = User(email="yahya@test.com", password="test", username="yahya")
yahya.save()

clothes = Category(name="Cloths", image='static/assets/images/clothes.jpg')
clothes.save()

electronics = Category(name="Electronics", image='static/assets/images/electronics.jpeg')
electronics.save()

home = Category(name="Home", image='static/assets/images/home.jpeg')
home.save()

product1 = Product(title='Laptop', price=1000, description='A laptop', quantity=10, category_id=electronics.id, image='static/assets/images/Laptop')
product1.save()

product2 = Product(title='T-Shirt', price=20, description='A T-Shirt', quantity=50, category_id=clothes.id, image='t-shirt.jpg')
product2.save()

product3 = Product(title='Chair', price=50, description='A chair', quantity=20, category_id=home.id, image='chair.jpg')
product3.save()

product4 = Product(title='Smartphone', price=500, description='A smartphone', quantity=15, category_id=electronics.id, image='smartphone.jpg')
product4.save()

product5 = Product(title='Dress', price=30, description='A dress', quantity=30, category_id=clothes.id, image='dress.jpg')
product5.save()

product6 = Product(title='Table', price=100, description='A table', quantity=10, category_id=home.id, image='table.jpg')
product6.save()

order1 = Order(user_id=amine.id)
order_item1 = Order_item(order_id=order1.id, price=100, quantity=10)
order1.save()
order_item1.save()

order2 = Order(user_id=ayoub.id)
order_item2 = Order_item(order_id=order2.id, price=100, quantity=10)
order2.save()
order_item2.save()

order3 = Order(user_id=mohamed.id)
order_item3 = Order_item(order_id=order3.id, price=100, quantity=10)
order3.save()
order_item3.save()

order4 = Order(user_id=yahya.id)
order_item4 = Order_item(order_id=order4.id, price=100, quantity=10)
order4.save()
order_item4.save()

cart1 = Cart(user_id=amine.id)
cart1.save()
cart2= Cart(user_id=ayoub.id)
cart2.save()
cart3 = Cart(user_id=mohamed.id)
cart3.save()
cart4 = Cart(user_id=yahya.id)
cart4.save()

cart_item1 = Cart_item(cart_id=cart1.id, product_id=product1.id, quantity=1)
cart_item1.save()
cart_item2 = Cart_item(cart_id=cart2.id, product_id=product2.id, quantity=1)
cart_item2.save()
cart_item3 = Cart_item(cart_id=cart3.id, product_id=product3.id, quantity=1)
cart_item3.save()
cart_item4 = Cart_item(cart_id=cart4.id, product_id=product4.id, quantity=1)
cart_item4.save()

products = storage.all(Product).values()
print(products)

