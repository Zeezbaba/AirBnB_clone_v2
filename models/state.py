#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
import models
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """getter attribute cities that
            returns the list of City instances
            """
            cities = models.storage.all(City)
            state_cities = []
            for city in cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
