#!/usr/bin/python3

import json
from models.base_model import BaseModel
import os

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    
    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w') as f:
            json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                for key, value in json_objects.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)

