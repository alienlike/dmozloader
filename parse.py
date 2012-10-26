#!/usr/bin/env python

from dmozparser.parser import DmozParser

DMOZ_FILE = '../dmoz/content.rdf.u8'

class TestHandler:
    def page(self, page, content):
        print page, content
    def finish(self): return

parser = DmozParser(DMOZ_FILE)
parser.add_handler(TestHandler())
parser.run()
