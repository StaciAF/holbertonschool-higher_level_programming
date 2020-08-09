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
    add_new_state = State(name='Louisiana')
    session.add(add_new_state)
    session.commit()
    print(add_new_state.id)
    session.close()
