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

    newState = State(name="California", cities=[City(name="San Francisco")])
    session.add(newState)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
