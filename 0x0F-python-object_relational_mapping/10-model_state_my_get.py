#!/usr/bin/pythonon3
"""
The script that prints the state object with the name passed
as arguement from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State

if __name__ == "__main__":
    """
    Gives access to the database to get the state object
    """
    db = 'mysql+_mysqldb//:{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.sql_query(state).filter(state.name == argv[4].first)

    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))
