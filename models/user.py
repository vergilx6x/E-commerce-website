#!/usr/bin/python3
""" holds class User"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    phone_number = Column(String(128), nullable=True)
    country = Column(String(128), nullable=True)
    city = Column(String(128), nullable=True)
    address = Column(String(128), nullable=True)
    postal_code = Column(String(60), nullable=True)
    image_url = Column(String(255), nullable=True)
    
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")
    carts = relationship("Cart", backref="user", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)