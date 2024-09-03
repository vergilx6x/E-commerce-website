#!/usr/bin/python3
""" holds class User"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
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
    favorites= Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)