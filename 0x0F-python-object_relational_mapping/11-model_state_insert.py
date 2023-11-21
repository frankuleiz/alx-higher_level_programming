#!/usr/bin/python3
"""
The script adds the state object "Louisana" to the 
database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Gives access to the database to add a state object
    """
    db = 'mysql+mysqldb//:{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    Session = sessionmaker(bind=engine)
    session = Session()

    lous = state(name='Louisiana')
    session.add(lous).add(lous)
    session.commit()
    print('{0}'.format(lous.id))
    session.close()
