from sqlalchemy import Column, Integer, String
from . import DeclarativeBase

class DmozPage(DeclarativeBase):

    __tablename__ = 'dmoz_page'

    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String)
    title = Column(String)
    description = Column(String)
    topic = Column(String)

    def __init__(self, page, content):
        self.url = page
        self.title = content.get(u'd:Title', u'')
        self.description = content.get(u'd:Description', u'')
        self.topic = content.get(u'topic', u'')