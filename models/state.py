#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
import os
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    storage_type = os.environ.get('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship(
                'City',
                backref='state',
                cascade='all, delete-orphan'
                )
    else:
        name = ""
        cities = []

    if (os.environ.get("HBNB_TYPE_STORAGE", "fs") == "fs"):
        @property
        def cities(self):
            '''
            returns the list of City instances with state_id
            equals to the current State.id
            '''
            city_list = []

            city_obj = models.storage.all(City)

            for key, value in city_obj.items():
                if value.state_id == self.id:
                    city_list.append(value)

            return city_list
