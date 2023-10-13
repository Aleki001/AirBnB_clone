#!/user/bin/python3

"""Defines Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represent Review
    Attributes:
        place_id (str): id of the place
        user_id (str): id of user
        text (str): text 
    """    
    place_id = ""
    user_id = ""
    text = ""
