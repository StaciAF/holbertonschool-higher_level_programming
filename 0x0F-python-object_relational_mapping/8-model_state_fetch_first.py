#!/usr/bin/python3
"""
this script lists all State obj from given db
"""


if __name__ == "__main__":
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_sql = session.query(State).order_by(State.id).first()
    if state_sql is None:
        print("Nothing")
    else:
        print("{}: {}".format(state_sql.id, state_sql.name))
    session.close()
