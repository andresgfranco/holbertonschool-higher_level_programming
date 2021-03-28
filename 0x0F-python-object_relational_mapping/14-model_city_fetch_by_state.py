#!/usr/bin/python3
"""Script that lists all City objects from the db
"""
from sys import argv
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Function that lists all City objects from the db"""
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

    for state, city in session.query(State, City).filter(
            City.state_id == State.id).all():
        print("{}: {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
