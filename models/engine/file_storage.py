#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User":User}


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
            Return the dictionary
        '''
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj = {}
        for key in self.__objects:
            obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                j = json.load(file)
            for key in j:
                self.__objects[key] = classes[j[key]["__class__"]](**j[key])
        except FileNotFoundError:
            pass
