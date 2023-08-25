#!/usr/bin/python3
"""
Connect model class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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

    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
