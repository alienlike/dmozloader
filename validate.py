from dmozparser.structure_parser import DmozStructureParser
from dmozparser.content_parser import DmozContentParser
from settings import DMOZ_CONTENT_FILE, DMOZ_STRUCTURE_FILE

class DummyHandler:
    def page(self, page, content):
        pass
    def topic(self, topic):
        pass
    def finish(self):
        pass

def validate_pages():

    print 'Validating pages...'

    # configure parser
    parser = DmozContentParser(DMOZ_CONTENT_FILE)
    parser.add_handler(DummyHandler())

    # run
    parser.run()

def validate_topics():

    print 'Validating topics...'

    # configure parser
    parser = DmozStructureParser(DMOZ_STRUCTURE_FILE)
    parser.add_handler(DummyHandler())

    # run
    parser.run()

if __name__ == '__main__':
    validate_topics()
    validate_pages()