#!/usr/bin/python3
"""Defines the city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
