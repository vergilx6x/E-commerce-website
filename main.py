#!/usr/bin/python3

from models.user import User
from models.product import Product
from models.category import Category

user = User(email="med@test.com", password="test")
category = Category(name="Cloths")
product = Product(title="Shoe", pric=100, quantity=20)

print(user)
print(category)
print(product)
user.save()
category.save()
product.save()
