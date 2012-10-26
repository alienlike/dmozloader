from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dmozparser.parser import DmozParser
from alchemyimport.alchemy_handler import AlchemyHandler

DMOZ_FILE = '../dmoz/content.rdf.u8'
CONN_STR = 'postgresql://localhost:5432/webstadex'

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