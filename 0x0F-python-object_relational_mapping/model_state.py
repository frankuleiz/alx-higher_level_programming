#!/usr/bin/python3
"""
The script contains the class definition of a state and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class state(Base):
    """
    State class

    Attributes:
        __tablename__(str): The tabke name of the class
        id (int): The state id of the state class
        name (str): The name of the state
    """
    __tablename__ = 'state'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
