from sqlalchemy import create_engine
from alchemyimport import DeclarativeBase

CONN_STR = 'postgresql://localhost:5432/webstadex'

if __name__ == '__main__':

    # build tables
    from alchemyimport.alchemy_handler import AlchemyHandler
    engine = create_engine(CONN_STR)
    DeclarativeBase.metadata.bind = engine
    DeclarativeBase.metadata.drop_all()
    DeclarativeBase.metadata.create_all(engine)