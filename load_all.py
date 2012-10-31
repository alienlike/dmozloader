from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dmozparser.parser import DmozParser
from handlers.alchemy_handler import AlchemyHandler
from settings import CONN_STR, DMOZ_FILE

if __name__ == '__main__':

    print 'Loading...'

    # configure session
    engine = create_engine(CONN_STR)
    Session = sessionmaker(bind=engine)
    session = Session()

    # configure parser
    parser = DmozParser(DMOZ_FILE)
    parser.add_handler(AlchemyHandler(session))

    # run
    parser.run()