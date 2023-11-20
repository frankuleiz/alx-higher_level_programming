#!/usr/bin/python3
"""
The script that prints the forst state object from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    The access to the database and get a state from from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(state).order_by(state_id).first()

    if instance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
