from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker
import random
from datetime import datetime

# Setting up the database
Base = declarative_base()
engine = create_engine('sqlite:///ecommerce.db')  # Replace with your actual database URL
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

# Defining the models

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock_quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    category = relationship('Category')

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User')

class CartItems(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    cart = relationship('Cart')
    product = relationship('Product')

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_amount = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User')

class OrdersItem(Base):
    __tablename__ = 'orders_item'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    order = relationship('Orders')
    product = relationship('Product')

# Create all tables
Base.metadata.create_all(engine)

# Generating random data

# Create Categories
categories = []
for _ in range(5):
    category = Category(
        name=fake.word().capitalize(),
        description=fake.text()
    )
    session.add(category)
    categories.append(category)
session.commit()

# Create Users
users = []
for _ in range(10):
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        password_hash=fake.sha256(),
    )
    session.add(user)
    users.append(user)
session.commit()

# Create Products
products = []
for _ in range(20):
    product = Product(
        name=fake.word().capitalize(),
        description=fake.text(),
        price=round(random.uniform(5.0, 100.0), 2),
        stock_quantity=random.randint(1, 100),
        category_id=random.choice(categories).id
    )
    session.add(product)
    products.append(product)
session.commit()

# Create Carts and Cart Items
for user in users:
    cart = Cart(user_id=user.id)
    session.add(cart)
    session.commit()

    for _ in range(random.randint(1, 5)):
        cart_item = CartItems(
            cart_id=cart.id,
            product_id=random.choice(products).id,
            quantity=random.randint(1, 5)
        )
        session.add(cart_item)
session.commit()

# Create Orders and Order Items
for user in users:
    if random.choice([True, False]):
        order = Orders(
            user_id=user.id,
            total_amount=round(random.uniform(20.0, 500.0), 2),
            status=random.choice(['pending', 'shipped', 'delivered', 'canceled'])
        )
        session.add(order)
        session.commit()

        for _ in range(random.randint(1, 5)):
            order_item = OrdersItem(
                order_id=order.id,
                product_id=random.choice(products).id,
                quantity=random.randint(1, 5),
                price=round(random.uniform(5.0, 100.0), 2)
            )
            session.add(order_item)
session.commit()

print("Random data inserted successfully!")
