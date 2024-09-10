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

mohamed = User(email="mohamed@test.com", password="test", username="mohamed")
mohamed.save()

yahya = User(email="yahya@test.com", password="test", username="yahya")
yahya.save()

clothes = Category(name="Clothes", image='static/assets/images/clothes.jpg')
clothes.save()

electronics = Category(name="Electronics", image='static/assets/images/electronics.jpeg')
electronics.save()

home = Category(name="Home", image='static/assets/images/home.jpeg')
home.save()

product1 = Product(name='Laptop', price=1000, description='A laptop', quantity=10, category_id=electronics.id)
product1.save()

product2 = Product(name='T-Shirt', price=20, description='A T-Shirt', quantity=50, category_id=clothes.id)
product2.save()

product3 = Product(name='Chair', price=50, description='A chair', quantity=20, category_id=home.id)
product3.save()

product4 = Product(name='Smartphone', price=500, description='A smartphone', quantity=15, category_id=electronics.id)
product4.save()

product5 = Product(name='Dress', price=30, description='A dress', quantity=30, category_id=clothes.id)
product5.save()

product6 = Product(name='Table', price=100, description='A table', quantity=10, category_id=home.id)
product6.save()

