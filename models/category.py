#!/usr/bin/python3
""" holds class Category"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

class Category(BaseModel, Base):

    __tablename__ = 'categories'
    name = Column(String(32), nullable=False)
    description = Column(Text, nullable=True)
    products = relationship("Product", backref="categories", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes category"""
        super().__init__(*args, **kwargs)