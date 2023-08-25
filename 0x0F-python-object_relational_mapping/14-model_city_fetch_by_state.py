#!/usr/bin/python3
"""
Connect model class to table in database
"""
import sys
from model_state import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    args = sys.argv
    host = "localhost" 
    passcode = args[2]
    user = args[1]
    database = args[3]
    port = 3306

    engine_config = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(user, passcode, host, port, database)
    engine = create_engine(engine_config)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State.name, City.id, City.name).filter_by(State.id == City.state_id)
    for row in data:
        print("{}: ({}) {}".format(data[0], data[1], data[2]))
