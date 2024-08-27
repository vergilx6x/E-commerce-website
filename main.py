#!/usr/bin/python3

from models.user import User
from models import storage

user = User(email="med@test.com", password="test")
print(user)
storage.new(user)
storage.save()