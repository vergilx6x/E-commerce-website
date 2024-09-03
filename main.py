#!/usr/bin/python3

import models
from models.user import User
from models.product import Product
from models.category import Category
from models.order import Order
from models.order_item import Order_item
from models.cart import Cart
from models.cart_item import Cart_item

user = User(email="med@test.com", password="test", username="veeerrrggrggll")
category = Category(name="Cloths")
product = Product(title="Shoe", pric=100, quantity=20, category_id=category.id)
order = Order(user_id=user.id)
order_item = Order_item(price=100, quantity=10)
cart = Cart(user_id=user.id)
cart_item = Cart_item(quantity=10)


print(user)
print(category)
print(product)

user.save()
category.save()
product.save()
order.save()
order_item.save()
cart.save()
cart_item.save()
