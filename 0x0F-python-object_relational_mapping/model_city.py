#!/usr/bin/python3
"""
The class definiton of the city module
"""
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class

    Attributes:
        __tablename__(str): The name of the table
        id (int): Unique identifier for each city
        state_id (int): Foreign key to reference a state in the database
        name (str): Name of the city
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('states.id'), nullable=False)
