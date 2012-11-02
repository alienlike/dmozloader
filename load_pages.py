from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dmozparser.content_parser import DmozContentParser
from handlers.page_handler import PageHandler
from settings import CONN_STR, DMOZ_CONTENT_FILE

if __name__ == '__main__':

    print 'Loading...'

    # configure session
    engine = create_engine(CONN_STR)
    Session = sessionmaker(bind=engine)
    session = Session()

    # configure parser
    parser = DmozContentParser(DMOZ_CONTENT_FILE)
    parser.add_handler(PageHandler(session))

    # run
    parser.run()