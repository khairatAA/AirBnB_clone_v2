#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime
import uuid
import models
from sqlalchemy import Column, Integer, String, MetaData, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
            str(uuid.uuid4()), String(60), unique=True,
            nullable=False, primary_key=True
            )

    created_at = Column(
            DateTime, nullable=False, default=datetime.utcnow()
                    )
    updated_at = Column(
            DateTime, nullable=False, default=datetime.utcnow()
                    )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
                    
        if kwargs:
            if 'updated_at' in kwargs and 'created_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )

                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                )

                del kwargs['__class__']
                self.__dict__.update(kwargs)
            else:
                """Handle case where updated at or created at is missing"""
                if 'created_at' not in kwargs:
                    kwargs['created_at'] = datetime.now()

                if 'updated_at' not in kwargs:
                    kwargs['updated_at'] = datetime.now()

                self.__dict__.update(kwargs)

            # create instance attribute from dict, if it’s not already the case
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)

            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        # from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
