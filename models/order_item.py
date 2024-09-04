#!/usr/bin/python3
""" holds class Order_items"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Order_item(BaseModel, Base):

    __tablename__ = 'order_items'
    order_id = Column(String(128), ForeignKey('orders.id') ,nullable=True)
    product_id = Column(String(128), ForeignKey('products.id'), nullable=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    order = relationship('Order', backref='order_items')
    product = relationship('Product', backref='order_items')

    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)


        

