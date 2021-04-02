#!/usr/bin/python3
""" python file that contains the class definition of a State """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ State class Args: Base(Object): Base class: """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
