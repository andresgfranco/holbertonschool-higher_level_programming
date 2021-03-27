#!/usr/bin/python3
"""Start link class to table in database
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

    for states in session.query(State).order_by(State.id).all():
        print("{}: {}".format(states.id, states.name))

    session.close()
