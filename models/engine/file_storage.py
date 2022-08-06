#!/usr/bin/python3
"""
Module to write a class FileStorage
"""
import json
from models.user import User
import os.path
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """
        new_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'Amenity': Amenity,
            'Place': Place,
            'City': City,
            'Review': Review
        }
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                new_dict = json.load(file)
            for key, value in new_dict.items():
                object = value['__class__']
                objects = object + '(**value)'
                self.__objects[key] = eval(objects)
