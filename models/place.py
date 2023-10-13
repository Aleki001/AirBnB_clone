#!/user/bin/python3

"""Defines Place class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """Represent Place
    Attributes:
        name (str): name of place
        city_id (str): id of city
        user_id (str): user's id
        description (str): description of the place
        number_rooms (int): no of rooms
        number_bathrooms (int): no of bathrooms
        max_guest (int): max no of guests
        price_by_night (int): night price
        latitude (float): latitude of place
        longitude (float): longitude of place
        amenity_ids (list): amenity ids"""
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
