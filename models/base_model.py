#!/usr/bin/python3

""" Base model for the AirBnB clone """

import uuid
from datetime import datetime
import models


class BaseModel():
    """ defines common attributes and methods in other classes"""
    def __init__(self, *args, **kwargs):
        """ instantiation of base model class
        Args:
            args: not used
            kwargs: constructor arguments
        Attributes:
            id: id generated by uuid
            created_at: time of creation
            updated_at: time of update
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime
                            .strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ returns stringrepresentation of the object """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates updated time with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

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
