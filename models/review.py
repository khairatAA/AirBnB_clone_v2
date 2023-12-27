#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os


class Review(BaseModel, Base):
    """ Review class to store review information """

    __tablename__ = 'reviews'

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        text = Column(String(1024), nullable=False)

        place_id = Column(
                String(60),
                ForeignKey('places.id'),
                nullable=False
                )

        user_id = Column(
                String(60),
                ForeignKey('users.id'),
                nullable=False
                )
    else:
        place_id = ""
        user_id = ""
        text = ""
