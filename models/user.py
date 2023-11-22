#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import models
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes s"""

    __tablename__ = 'users'

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        email = Column(String(128), nullable=False)

        password = Column(String(128), nullable=False)

        first_name = Column(String(128), nullable=True)

        last_name = Column(String(128), nullable=True)

        places = relationship("Place",
                              backref="user",
                              cascade="all, delete-orphan")
    else:
        email = ""
        password = ''
        first_name = ''
        last_name = ''
        places = []
    '''
    reviews = relationship("Review",
                           backref="user",
                           cascade="all, delete-orphan")
    '''
