#!/usr/bin/python3
import uuid
from datetime import datetime
import re
class User:
    
    def __init__(self, email: str, first_name='', last_name='', is_admin=False):
        self.id =  str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.places = set()

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if len(value) > 50:
            raise ValueError('First name must not exceed 50 characters')
        else:
            self.__first_name = value
            self.updated_at = datetime.now()

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) > 50:
            raise ValueError('Last name must not exceed 50 characters')
        else:
            self.__last_name = value
            self.updated_at = datetime.now()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(pattern, value):
            raise ValueError(f"Invalid email format: {value}")
        self.__email = value
        self.updated_at = datetime.now()
    
    def update(self, update_dict):
        for key in update_dict:
            if hasattr(self, key):
                setattr(self, key, update_dict[key])
                self.updated_at = datetime.now()
            else:
                raise ValueError('You Enter The Wrong attribute')
    
    def Delete_User(self):
        pass
        
    def craete_place(self, title, description, price, latitude, longitude):
        from place import Place
        new_place = Place(title, price, latitude, longitude, self, description)
        self.places.add(new_place.id)
        self.updated_at = datetime.now()
        return new_place
    

    def delete_place(self, value):
        pass

    def list_place(self):
        return self.places
