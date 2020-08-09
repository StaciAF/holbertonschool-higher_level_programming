#!/usr/bin/python3
"""
this script lists all City obj from given db
"""


if __name__ == "__main__":
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).filter(
            City.state_id == State.id).order_by(City.id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
