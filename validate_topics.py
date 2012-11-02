from dmozparser.structure_parser import DmozStructureParser
from settings import DMOZ_STRUCTURE_FILE

class DummyHandler:
    def topic(self, topic): pass
    def finish(self): pass

if __name__ == '__main__':

    print 'Validating...'

    # configure parser
    parser = DmozStructureParser(DMOZ_STRUCTURE_FILE)
    parser.add_handler(DummyHandler())

    # run
    parser.run()