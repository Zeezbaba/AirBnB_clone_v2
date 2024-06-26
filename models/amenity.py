#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models
import sqlalchemy


class Amenity(BaseModel, Base):
    """Updating Amenity """
    __tablename__ = 'amenities'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        """__tablename__ = 'amenities'"""
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
