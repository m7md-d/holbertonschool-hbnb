#!/usr/bin/python3
import uuid
from datetime import datetime

class Amenity:
    
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if len(value) > 50:
            raise ValueError('the name should be less than 50 characters')
        else:
            self.__name = value
            self.updated_at = datetime.now()

    def update(self, update_dict):
        for key in update_dict:
            if hasattr(self, key):
                setattr(self, key, update_dict[key])
                self.updated_at = datetime.now()
            else:
                raise ValueError('theres no attribute in this name')
