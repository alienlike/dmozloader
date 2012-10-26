from dmozparser.parser import DmozParser

DMOZ_FILE = '../dmoz/content.rdf.u8'

class DummyHandler:
    def page(self, page, content): pass
    def finish(self): pass

if __name__ == '__main__':

    print 'Validating...'

    # configure parser
    parser = DmozParser(DMOZ_FILE)
    parser.add_handler(DummyHandler())

    # run
    parser.run()