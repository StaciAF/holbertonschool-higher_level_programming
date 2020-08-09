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
    delete_a_sql = session.query(State).filter(State.name.like('%a%')).first()
    while (delete_a_sql is not None):
        session.delete(delete_a_sql)
        delete_a_sql = session.query(State).filter(
            State.name.like('%a%')).first()
    session.commit()
    session.close()
