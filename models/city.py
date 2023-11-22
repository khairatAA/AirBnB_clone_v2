#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    storage_type = os.environ.get('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(
                String(60),
                ForeignKey("states.id"), nullable=False
                )
    else:
        name = ""
        state_id = ""
