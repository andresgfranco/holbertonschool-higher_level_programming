#!/usr/bin/python3
""" script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(mysql_username,
                                                           mysql_password,
                                                           database_name))

    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    queryState = session.query(State).order_by(State.id).all()

    for state in queryState:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
