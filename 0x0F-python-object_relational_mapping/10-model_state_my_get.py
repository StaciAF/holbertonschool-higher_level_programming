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
    st_name_arg = argv[4]
    for state_name_sql in session.query(State).order_by(State.id).all():
        if state_name_sql.name == st_name_arg:
            print("{}".format(state_name_sql.id))
            break
    else:
            print("Not Found")
    session.close()
