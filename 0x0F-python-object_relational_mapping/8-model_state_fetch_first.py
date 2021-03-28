#!/usr/bin/python3
"""Script that prints the first State object from db
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Function that lists all State objects from the db"""
    credentials = {
        "host": "localhost",
        "port": "3306",
        "user": argv[1],
        "pass": argv[2],
        "db": argv[3]}

    str_format = 'mysql+mysqldb://{user}:{pass}@{host}:{port}/{db}'
    engine = create_engine(str_format.format(
        **credentials), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State):
        if states:
            print("{}: {}".format(states.id, states.name))
            break
        else:
            print("Nothing")
            break

    session.close()
