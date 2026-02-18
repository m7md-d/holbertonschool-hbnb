#!/usr/bin/python3
import uuid
from datetime import datetime
from user import User

class Place:

    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner: User, description=''):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.reviews = []
        self.amenities = set()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) > 100:
            raise ValueError('Title must be 100 characters or less')
        else:
            self.__title = value
            self.updated_at = datetime.now()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price must be a positive value')
        else:
            self.__price = float(value)
            self.updated_at = datetime.now()

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90 or value > 90:
            raise ValueError('Latitude must be between -90.0 and 90.0')
        else:
            self.__latitude = value
            self.updated_at = datetime.now()

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180 or value > 180:
            raise ValueError('Longitude must be between -180.0 and 180.0')
        else:
            self.__longitude = value
            self.updated_at = datetime.now()

    @property
    def owner(self):
        return self.__owner_id

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise TypeError('Owner must be an instance of User')
        else:
            self.__owner_id = value.id
            self.updated_at = datetime.now()


     def update(self, update_dict):
        for key in update_dict:
            if hasattr(self, key):
                setattr(self, key, update_dict[key])
                self.updated_at = datetime.now()
            else:
                raise ValueError('You Enter The Wrong attribute')
   


    def add_review(self, value):
        from review import Review
        if not isinstance(value, Review):
            raise TypeError('Value must be an instance of Review')
        else:
            self.reviews.append(value.id)
            self.updated_at = datetime.now()

    def delete_review(self, value):
        from review import Review
        if not isinstance(value, Review):
            raise TypeError('Value must be an instance of Review')
        else:
            if value.id in self.reviews:
                self.reviews.remove(value.id)
                self.updated_at = datetime.now()
            else:
                raise ValueError('Review not found')
    
    def list_review(self):
        return self.reviews

    def add_amenity(self, value):
        from amenity import Amenity
        if not isinstance(value, Amenity):
            raise TypeError('Value must be an instance of Amenity')
        else:
            self.amenities.add(value.id)
            self.updated_at = datetime.now()

    def delete_amenity(self, value):
        from amenity import Amenity
        if not isinstance(value, Amenity):
            raise TypeError('Value must be an instance of Amenity')
        else:
            if value.id in self.amenities:
                self.amenities.remove(value.id)
                self.updated_at = datetime.now()
            else:
                raise ValueError('Amenity not found')

    def list_amenity(self):
        return self.amenities
