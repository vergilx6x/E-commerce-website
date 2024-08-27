#!/usr/bin/python

from models.base_model import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:

    _engine = None
    _session = None

    def __init__(self):

        mysql_user = "root"
        mysql_pwd = ""
        mysql_db = "website_db"
        