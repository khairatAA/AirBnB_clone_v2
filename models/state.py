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

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship(
                'City',
                backref='state',
                cascade='all, delete-orphan'
                )

    if storage_type == 'fs':
        name = ''

        @property
        def cities(self):
            '''
            returns the list of City instances with state_id
            equals to the current State.id
            '''
            city_list = []

            city_objs = models.storage.all(City)

            for city_obj in city_objs.values():
                if city_obj.state_id == self.id:
                    city_list.append(city_obj)

            return city_list
