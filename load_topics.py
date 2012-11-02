from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dmozparser.structure_parser import DmozStructureParser
from handlers.topic_handler import TopicHandler
from settings import CONN_STR, DMOZ_STRUCTURE_FILE

if __name__ == '__main__':

    print 'Loading...'

    # configure session
    engine = create_engine(CONN_STR)
    Session = sessionmaker(bind=engine)
    session = Session()

    # configure parser
    parser = DmozStructureParser(DMOZ_STRUCTURE_FILE)
    parser.add_handler(TopicHandler(session))

    # run
    parser.run()