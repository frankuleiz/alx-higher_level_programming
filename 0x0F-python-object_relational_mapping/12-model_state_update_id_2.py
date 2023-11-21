#!/usr/bin/python3
"""
The script that changes the name of a state object from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, State

if __name__ == "__main__":
    """
    Gives access to the database to change the state object
    in the database
    """
    db = 'mysql+mysqldb://{}:{}@localhost{}/'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = session.query(state).filter(state.id == '2').first()
    state_name.name = 'New Mexico'
    session.commit()
    session.close()
