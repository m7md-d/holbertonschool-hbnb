#!/usr/bin/python3
import uuid
from datetime import datetime
from user import User
from place import Place

class Review:
    
    def __init__(self, text: str, rating: int, place: Place, user: User):
        self.id = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.created_at = datetime.now()
        self.updated_at =  self.created_at

    @property
    def rating(self):
        return self.__rating
    @property
    def place(self):
        return self.__place_id
    @property
    def user(self):
        return self.__user_id

    @rating.setter
    def rating(self, value):
        if value < 1 or value > 5:
            raise ValueError('the rating should be between 1 and 5')
        else:
            self.__rating = value
            self.updated_at = datetime.now()
    
    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise TypeError('should Enter Place')
        else:
            self.__place_id = value.id
            self.updated_at = datetime.now()

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError('should Enter User')
        else:
            self.__user_id = value.id
            self.updated_at = datetime.now()

    def update(self, update_dict):
        
        for key in update_dict:
            if hasattr(self, key):
                setattr(self, key, update_dict[key])
                self.updated_at = datetime.now()
            else:
                raise ValueError('no attrebut in this name')
