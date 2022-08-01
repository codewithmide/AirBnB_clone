#!/usr/bin/python3
"""
Storage for all files
"""
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes all instances to a JSON field
    and deserialize file to instances
    """
# __file_path: string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
# __objects: dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """
        return all
        """
        return self.__objects
