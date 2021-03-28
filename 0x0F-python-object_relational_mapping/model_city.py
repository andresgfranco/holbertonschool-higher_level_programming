#!/usr/bin/python3
"""class definition of a City"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
Base = __import__('model_state').Base


class City(Base):
    """Class City inhereted from Base"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
