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
    flag = 0
    for state_name_sql in session.query(State).filter(State.name == argv[4]).all():
            print("{}".format(state_name_sql.id))
            flag = 1
    if flag is 0:
        print("Not Found")
    session.close()
