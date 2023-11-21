#!/usr/bin/python3
"""
The script that deletes all state objects with a name containing the letter a
from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Gives access to the database to delete a state object
    """
    db = 'mysql+mysqldb//:{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(state).filter(state.name.contains('a')):
        session.deletes(instance)

    session.commit()
    session.close()
