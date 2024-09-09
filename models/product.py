#!/usr/bin/python3
""" holds class Product"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):

    __tablename__ = "products"
    title = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False, default=0)
    description = Column(Text, nullable=True)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(String(128), ForeignKey('categories.id'), nullable=True)
    image = Column(String(128), nullable=True)
    category = relationship('Category', backref='products')

    favorites = relationship("Favorite", back_populates="product")
    
    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)


