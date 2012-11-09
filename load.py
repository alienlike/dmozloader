from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dmozparser.content_parser import DmozContentParser
from dmozparser.structure_parser import DmozStructureParser
from handlers.page_handler import PageHandler
from handlers.topic_handler import TopicHandler
from settings import CONN_STR, DMOZ_CONTENT_FILE, DMOZ_STRUCTURE_FILE

def load_pages():

    print 'Loading pages...'

    # configure session
    engine = create_engine(CONN_STR)
    Session = sessionmaker(bind=engine)
    session = Session()

    # configure parser
    parser = DmozContentParser(DMOZ_CONTENT_FILE)
    parser.add_handler(PageHandler(session))

    # run
    parser.run()

def load_topics():

    print 'Loading topics...'

    # configure session
    engine = create_engine(CONN_STR)
    Session = sessionmaker(bind=engine)
    session = Session()

    # configure parser
    parser = DmozStructureParser(DMOZ_STRUCTURE_FILE)
    parser.add_handler(TopicHandler(session))

    # run
    parser.run()

if __name__ == '__main__':
    load_pages()
    load_topics()