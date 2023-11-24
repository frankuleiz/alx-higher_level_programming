#!/usr/bin/python3
"""
The script prints all the city objects
from the database
"""

from sqlalchemy import create_engine
from sqlalchemy import Session, sessionmaker
from model_city import City
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    Gives access to the database to get the cities
    object from the database
    """
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).join(State)

    for city, state in query.all():
        print("{}: ({:d}), {}".format(state, city.id, city.name))

    session.commit()
    session.close()
