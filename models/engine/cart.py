#!/usr/bin/python3
""" holds class User"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String

class Cart(BaseModel, Base):