from sqlalchemy import create_engine
from models import DeclarativeBase
from settings import CONN_STR

def build_tables():

    print 'Building tables...'

    # build tables
    from models.dmoz_page import DmozPage
    from models.dmoz_topic import DmozTopic
    engine = create_engine(CONN_STR)
    DeclarativeBase.metadata.bind = engine
    DeclarativeBase.metadata.drop_all()
    DeclarativeBase.metadata.create_all(engine)

if __name__ == '__main__':
    build_tables()