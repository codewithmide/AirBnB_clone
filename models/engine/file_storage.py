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
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
# BaseModel.12121212
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        class_dict = {
            "BaseModel": BaseModel,
        }

        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                json_read = json.load(file)
                for keys, value in json_read.items():
                    class_name = value["__class__"]
                    self.new(class_dict[class_name](**value))
        except FileNotFoundError:
            pass

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json_obj = self.__objects.copy()
        for key, val in self.__objects.items():
            json_obj[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(json_obj))
