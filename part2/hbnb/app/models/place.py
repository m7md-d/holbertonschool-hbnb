#!/usr/bin/python3
import uuid
from datetime import datetime
from app.models.basemodel import BaseModel


class Place(BaseModel):

    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner, description=''):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
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
            super().save()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price must be a positive value')
        else:
            self.__price = float(value)
            super().save()

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90 or value > 90:
            raise ValueError('Latitude must be between -90.0 and 90.0')
        else:
            self.__latitude = value
            super().save()

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180 or value > 180:
            raise ValueError('Longitude must be between -180.0 and 180.0')
        else:
            self.__longitude = value
            super().save()

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        from app.models.user import User
        if not isinstance(value, User):
            raise TypeError('Owner must be an instance of User')
        else:
            self.__owner = value
            super().save()


   


    def add_review(self, value):
        from app.models.review import Review
        if not isinstance(value, Review):
            raise TypeError('Value must be an instance of Review')
        else:
            self.reviews.append(value.id)
            super().save()


    def add_amenity(self, value):
        from app.models.amenity import Amenity
        if not isinstance(value, Amenity):
            raise TypeError('Value must be an instance of Amenity')
        else:
            self.amenities.add(value.id)
            super().save()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': {
                'id': self.owner.id,
                'first_name': self.owner.first_name,
                'last_name': self.owner.last_name,
                'email': self.owner.email
            }
        }
