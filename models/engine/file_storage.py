#!/usr/bin/python3
"""storage"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    """storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ save as json string"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """convert from json to python3"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                new_obj_dict = json.load(f)
                for ob in new_obj_dict.values():
                    class_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_name)(**ob))
        except FileNotFoundError:
            pass
