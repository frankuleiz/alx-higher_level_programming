#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(state).order_by(states.id):
        print('{0}: {1}'.format(instance.id, instance.name))
