from build_tables import build_tables
from validate import *
from load import *

if __name__ == '__main__':
    validate_topics()
    validate_pages()
    build_tables()
    load_topics()
    load_pages()