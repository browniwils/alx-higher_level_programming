#!/usr/bin/python3
"""
Connect model class to table in database
"""
import sys
from relationship_state import Base, State
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
    engine = create_engine(engine_config, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    data = Session.query(State).order_by(State.id)
    for row in data:
        print(row.id, row.name, sep=": ")
        for city in row.cities:
            print("    ", end="")
            print(city.id, city.name, sep=": ")
