#!/usr/bin/python3

""" Base model for the AirBnB clone """

import uuid
from datetime import datetime

class BaseModel():
    """ defines common attributes and methods in other classes"""
    def __init__(self):
        """ instantiation of base model class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ returns stringrepresentation of the object """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates updated time with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns dictionary representation of the object"""
        dict_formed = {}
        dict_formed["__class__"] = self.__class__.__name__
        
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_formed[key] = value.isoformat()
            else:
                dict_formed[key] = value

        return dict_formed
