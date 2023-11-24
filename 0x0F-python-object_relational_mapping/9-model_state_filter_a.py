#!/usr/bin/python3
"""
The script lists all state bjects that contain the
letter 'a' from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    """
    Gives access to the database and get a state from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[1], sys.argv[1], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(state).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))
