#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(
                String(60),
                ForeignKey('cities.id'),
                nullable=False
                )

        user_id = Column(
                String(60),
                ForeignKey('users.id'),
                nullable=False
                )

        name = Column(
                String(128),
                nullable=False
                )

        description = Column(
                String(1024)
                )

        number_room = Column(
                Integer,
                nullable=False,
                default=0
                )

        number_bathrooms = Column(
                Integer,
                nullable=False,
                default=0
                )

        max_guest = Column(
                Integer,
                nullable=False,
                default=0
                )

        price_by_night = Column(
                Integer,
                nullable=False,
                default=0
                )

        latitude = Column(
                Float,
                nullable=True
                )

        longitude = Column(
                Float,
                nullable=True
                )

        reviews = relationship(
                "Review",
                backref="place",
                )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

    @property
    def reviews(self):
        """
        for FileStorage: getter attribute reviews that returns
        the list of Review instances with place_id equals to the current
        Place.id => It will be the FileStorage relationship
        between Place and Review
        """

        matching_reviews = []

        matching_obj = models.storage.all(Review)

        for key, value in matching_obj.items():
            if value.place_id == self.id:
                matching_reviews.append(value)

        return matching_reviews
