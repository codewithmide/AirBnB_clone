#!/usr/bin/python3
# A UUID (Universal Unique Identifier) is used to uniquely identify an object.
# datetime is a built-in python module for date and time
# Models is the module created for this project. (it is not python in-built)
from uuid import uuid4
from datetime import datetime
import models
"""
The BaseModel module
"""


# the date and time format
fdateAndTime = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """
    A class that defines all common attributes/methods for other classes:
    Public instance attributes:
    id: string - assign with an uuid when an instance is created
    The goal is to have a unique id for each BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        This method initializes all attributes under the BaseModels
        """
# *args (Non-Keyword Arguments)
# **kwargs (Keyword Arguments)
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
                    if hasattr(self, 'created_at') and type(
                            self.created_at) is str:
                        self.created_at = datetime.strptime(
                            kwargs["created_at"], fdateAndTime)
                    if hasattr(self, 'updated_at') and type(
                            self.updated_at) is str:
                        self.updated_at = datetime.strptime(
                            kwargs["updated_at"], fdateAndTime)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        This public instance method should print:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        This public instance method returns a string representation
        """
        return self.__str__()

    def save(self):
        """
        updates the attribute updated_at with the current date and time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
