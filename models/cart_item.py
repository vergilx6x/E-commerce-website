#!/usr/bin/python3
""" holds class cart_item"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship

class Cart_item(BaseModel, Base):

    __tablename__ = 'cart_items'
    cart_id = Column(String(128), ForeignKey('carts.id'), nullable=True)
    product_id = Column(String(128), ForeignKey('products.id'), nullable=True)
    quantity = Column(Integer, nullable=False, default=1)
    cart = relationship("Cart", backref="cart_items")
    product = relationship("Product", backref='cart_items')

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)