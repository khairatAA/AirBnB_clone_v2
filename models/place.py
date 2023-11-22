#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False)
    user_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    
    @property
    def reviews(self):
        """
        for FileStorage: getter attribute reviews that returns
        the list of Review instances with place_id equals to the current
        Place.id => It will be the FileStorage relationship
        between Place and Review
        """
        from models import storage
        d_review = storage.all(Review)
        matching_reviews = [
            review for review in d_review.values() if review.place_id == self.id
        ]
        return matching_reviews
