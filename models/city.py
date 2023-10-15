#!/user/bin/python3

"""Defines City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent State
    Attributes:
        name (str): name of state
        state_id (str): id of the state"""

    state_id = ""
    name = ""
