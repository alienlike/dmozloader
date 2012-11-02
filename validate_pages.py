from dmozparser.content_parser import DmozContentParser
from settings import DMOZ_CONTENT_FILE

class DummyHandler:
    def page(self, page, content): pass
    def finish(self): pass

if __name__ == '__main__':

    print 'Validating...'

    # configure parser
    parser = DmozContentParser(DMOZ_CONTENT_FILE)
    parser.add_handler(DummyHandler())

    # run
    parser.run()