#!/usr/bin/python3
""" holds class Product"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, ForeignKey

class Product(BaseModel, Base):

    __tablename__ = "products"
    title = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False, default=0)
    description = Column(Text, nullable=True)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(String(128), ForeignKey('categories.id'), nullable=False)
    image = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)


